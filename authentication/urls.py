from django.conf.urls import url
from authentication.views import RegistrationAPIView, LoginAPIView, UserListViewSet
# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^users/$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    path('api/', include('apps.api.urls'))
]
