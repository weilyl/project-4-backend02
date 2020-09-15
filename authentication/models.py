from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# allows us to set the JWT settings
from rest_framework_jwt.settings import api_settings

# setting JWT payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your models here.
class UserManager(BaseUserManager):
    # don't care if first or last names are given
    # password is none by default
    def create_user(self, username, email, password=None, first_name=None, last_name=None):
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email address")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=False
        )

        user.set_password(password)
        # creating the user
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # default True for testing purposes
    created_at = models.DateTimeField(auto_now_add=True)  # when user is first created, get system time & freeze info
    updated_at = models.DateTimeField(auto_now=True)  # get current time

    USERNAME_FIELD = 'username'  # doesn't need brackets bc of Base User inheritance so Django checks for it
    REQUIRED_FIELDS = ['email']  # brackets indicate MUST be present; indicates list of info that is required

    # telling Django that UserManager class (as defined above) should manage objects of this type
    # explicitly directing Django not to use built-in managers
    objects = UserManager()

    def __str__(self):
        return self.username

    @property  # whenever user is created dynamically, look for this method
    def token(self):
        # generate token & return it every time user is created
        return self._generate_jwt_token()  # private method so need to be implemented somewhere else

    def _generate_jwt_token(self):  # unlike Ruby (Rails), can define after it is called
        """
        generates a JSON Web Token that stores this(self) or current object
        aka this user's instance
        and has an expiry date set to 60 days into the future (configure +settings.py)
        :return:
        """
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token
