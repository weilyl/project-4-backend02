# Project Overview

## Project

Link to completed project [here](https://goodhooks.herokuapp.com/)

Link to project frontend [here]()

Link to project backend [here](https://github.com/weilyl/project-4-backend02)

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.

You are **responsible** for scheduling time with your squad to seek approval for each deliverable by the end of the corresponding day, excluding `Saturday` and `Sunday`.

| Day   | Deliverable                                                      | Status     |
| ----- | ---------------------------------------------------------------- | ---------- |
| Day 1 | Project Description                                              | Complete   |
| Day 1 | Wireframes / Priority Matrix / Timeline `backend` and `frontend` | Complete   |
| Day 2 | Backend: Functioning auth, models                                | Complete   |
| Day 3 | Backend: Functioning RESTful API                                 | Complete   |
| Day 4 | Frontend: MVP Vue components & auth methods                      | Complete   |
| Day 5 | Frontend: MVP Vue CRUD methods                                   | Complete   |
| Day 6 | Frontend: Finishing touches                                      | Complete   |

## Project Description

User Model: 
- username
- password
- email
- first name
- last name

List Model
- name
- owner
- description

Link Model
- list
- name
- description
- image URL

## Time/Priority Matrix

[Here]() is a full list of features that have been prioritized based on the `Time and Priority` Matix.

### MVP/PostMVP

#### MVP

- JWT Authentication/Authorization testing
- User model, serializers, views, urls
- Link model, serializers, views, urls
- List model, serializers, views, urls
- Migration
- Deploy and test on Heroku
- Test on Postman/Django Admin

#### PostMVP

- tags per link (public and/or private)
- image scraping from URL for each link
- filter by difficulty (user-assigned), medium (video/text), project type (blanket, scarf, hat, etc.) 

#### Post-Post-MVP
- public reviews (rate: technical difficulty, ease of comprehension, aesthetic)
- contact form to remove copyrighted patterns

## Functional Components

#### MVP

| Component               | Priority | Estimated Time | Time Invested | Actual Time |
| ----------------------- | :------: | :------------: | :------------: | :---------: |
| JWT Auth                |    H     |      3hr       |      10hr      |     1hr     |
| User model              |    H     |      1hr       |      5hr       |     -hr     |
| User serializers        |    M     |      1hr       |      -hr       |     -hr     |
| User views              |    H     |      1hr       |      5hr       |     -hr     |
| User urls               |    M     |      1hr       |      2hr       |     -hr     |
| List Model              |    M     |      2hrs      |      -hr       |     -hr     |
| List serializers        |    M     |      2hr       |      -hr       |     -hr     |
| List views              |    H     |      2hr       |      -hr       |     -hr     |
| List urls               |    M     |      1hr       |      -hr       |     -hr     |
| Link Model              |    M     |      2hrs      |      -hr       |     -hr     |
| Link serializers        |    M     |      2hr       |      -hr       |     -hr     |
| Link views              |    H     |      2hr       |      -hr       |     -hr     |
| Link urls               |    M     |      1hr       |      -hr       |     -hr     |
| Test on Postman         |    L     |      5hr       |      -hr       |     -hr     |
| Deploy                  |    L     |      10hr      |      -hr       |     3hr     |
| Total                   |    H     |    27.5 hrs    |      -hrs      |    7hrs     |

#### PostMVP

| Component                                        | Priority | Estimated Time | Time Invested  | Actual Time |
| ------------------------------------------------ | :------: | :------------: | :------------: | :---------: |
| Tag model, serializers, views, urls              |    M     |      3hr       |      -hr       |     -hr     |
| Review model, serializers, views, urls           |    H     |      2hr       |      2hrs      |     2hrs    |
| Filters                                          |    M     |      5hr       |      -hr       |     -hr     |
| Contact form                                     |    H     |      5hr       |      -hr       |     -hr     |
| Image scraper                                    |    L     |      10hr      |      -hr       |     -hr     |
| Total                                            |    H     |     25hrs      |      2hrs      |    2hrs     |

## Additional Libraries

- Django

## Code Snippet


```

```


## Issues and Resolutions


**ERROR**: 

**RESOLUTION**: 



**ERROR**: After registering models in admin.py to test API views & routes in Django Admin:

```    raise RuntimeError(
RuntimeError: Model class apps.api.models.Tag doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
```

**RESOLUTION**: Tried to unregister unused (post-MVP) models, but same error occurred. 
Tried to follow [this](https://stackoverflow.com/questions/55553252/runtimeerror-model-class-xxx-doesnt-declare-an-explicit-app-label-and-isnt-in) and use absolute import rather than relative import, but same error occurred.
Tried to be more explicit in settings.py > INSTALLED_APPS by using `'apps.api.apps.APIConfig'` and `'apps.api.apps' instead of `'apps.api'`.
Further down in above link, suggestions are to add class Meta & app_label attribute but the following error occurred:

```
raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Cannot import 'api'. Check that 'apps.api.apps.APIConfig.name' is correct.
```

Note: `apps.api` in INSTALLED_APPS did not raise any errors in previous migrations. 
Final Resolution: Returned to using `'apps.api'` in INSTALLED_APPS.

**ERROR**: 2020-09-16 When attempting to make migrations after fixing below errors: 

```
ERROR: 
SystemCheckError: System check identified some issues:

ERRORS:
api.List.owner: (fields.E300) Field defines a relation with model 'authorization.User', which is either not installed, or is abstract.
api.List.owner: (fields.E307) The field api.List.owner was declared with a lazy reference to 'authorization.user', but app 'authorization' isn'
t installed.
```

**RESOLUTION**: Fixed a spelling error - "authorization.user" reference in the API models should have been "authentication.user".


**ERROR**: 2020-09-16 When trying to make migrations after adding new Tag class to models:
```
SystemCheckError: System check identified some issues:

ERRORS:
api.List.owner: (fields.E300) Field defines a relation with model 'authorization.User', which is either not installed, or is abstract.
api.List.owner: (fields.E307) The field api.List.owner was declared with a lazy reference to 'authorization.user', but app 'authorization' isn'
t installed.
authentication.User.favorites: (fields.E304) Reverse accessor for 'User.favorites' clashes with reverse accessor for 'User.saved'.
        HINT: Add or change a related_name argument to the definition for 'User.favorites' or 'User.saved'.
authentication.User.saved: (fields.E304) Reverse accessor for 'User.saved' clashes with reverse accessor for 'User.favorites'.
        HINT: Add or change a related_name argument to the definition for 'User.saved' or 'User.favorites'.
```

**RESOLUTION**: Added `related_name` for favorites & saved items in User model.


**ERROR**: 2020-09-16 When making migration file:

```
File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 22, in Link
    tags = models.ManyToManyField(blank=True)
TypeError: __init__() missing 1 required positional argument: 'to'
```

**RESOLUTION**: Following [this link](https://viblo.asia/p/make-simple-tag-function-with-djangos-manytomany-relationship-model-V3m5WbnblO7), new class Tag was added to models.py so that tags attribute in Link model can refer to a table in the ManyToManyField arguments

**ERROR**: 2020-09-16 11:54am Fixed previous error, still attempting to make migrations files:

```
File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py", line 5, in <module>
    from apps.api.models import Link, List
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 2, in <module>
    from authentication.models import User
ImportError: cannot import name 'User' from partially initialized module 'authentication.models' (most likely due to a circular import) (/mnt/c
/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py)
```

Attempted resolution: commenting out User model to write one migration file at a time

**RESOLUTION**: Thanks to Ebony for having the same issue before me & Jeremy for helping her resolve it, I removed the User model import into the api models.py and instead used a string of "authentication.user" as the reference in the Links model.

Result of above error (prior to fixing circular import): 

```
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/authentication/models.py", line 9, in <module>
    import apps.api.models
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 17, in <module>
    class Link(models.Model):
  File "/mnt/c/Users/weily/Documents/seir-6-29/student/unit04/project04/p04backend/apps/api/models.py", line 18, in Link
    list = models.ForeignKey(List, related_name='lists')
TypeError: __init__() missing 1 required positional argument: 'on_delete'
```

Attempt: Added an `on_delete=DO_NOTHING()` argument

Result: `TypeError: DO_NOTHING() missing 4 required positional arguments: 'collector', 'field', 'sub_objs', and 'using'`

**RESOLUTION**: Removed `()` from `DO_NOTHING`


**ERROR**: 2020-09-16 11:45am Edited User model, then made migrations files: `TypeError: __init__() got an unexpected keyword argument 'Null'`

**RESOLUTION**: Learned that URLField in Django cannot have `blank=True`


**ERROR**: 2020-09-15 12:04pm When deploying to Heroku after authentication successfully tested locally via Postgres:
```
/app/.heroku/python/lib/python3.6/site-packages/environ/environ.py:630: UserWarning: /app/p04backend/.env doesn't exist - if you're not configuring your environment separately, create one.
  "environment separately, create one." % env_file)
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)	
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 85, in wrapped
    res = handle_func(*args, **kwargs)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/commands/makemigrations.py", line 101, in handle
    loader.check_consistent_history(connection)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/db/migrations/loader.py", line 306, in check_consistent_history
    connection.alias,
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency authentication.0001
_initial on database 'default'.
```

**RESOLUTION**: Reset database on heroku side: `sudo heroku pg:reset --app=goodhooks`


**ERROR**: `ModuleNotFound`

**RESOLUTION**: Added authentication directory to `INSTALLED_APPS` list in `settings.py`


**ERROR**: 2020-09-12 to 2020-09-15: Python requirements kept disappearing when configuring interpreter for virtual environment in PyCharm settings.

**RESOLUTION**: PyCharm Pro does not support Python interpreters installed on WSL2 for virtual environments, only globally. A second backend repo was made from scratch, with a virtual environment created and activated in Ubuntu.
