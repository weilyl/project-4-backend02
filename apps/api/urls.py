from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import ListViewSet, ListLinks, SingleLinkPerList, LinksViewSet

router = routers.DefaultRouter()
router.register('lists', ListViewSet, basename='lists')
router.register('links', LinksViewSet, basename='links')

custom_urlpatterns = [
   url(r'lists/(?P<list_pk>\d+)/links$', ListLinks.as_view(), name='list_links'),
   url(r'lists/(?P<list_pk>\d+)/links/(?P<pk>\d+)$', SingleLinkPerList.as_view(), name='single_link_in_list')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

