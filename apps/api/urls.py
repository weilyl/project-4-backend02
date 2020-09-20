from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import ListViewSet, ListLinksViewSet, SingleLinkPerList, LinksViewSet, \
   RemoveLinkFromListView, AddLinkToListView

router = routers.DefaultRouter()
router.register('lists', ListViewSet, basename='lists')
router.register('links', LinksViewSet, basename='links')

custom_urlpatterns = [
   url(r'lists/(?P<list_pk>\d+)/links$', ListLinksViewSet.as_view(), name='list_links'),
   url(r'lists/(?P<list_pk>\d+)/links/(?P<pk>\d+)$', SingleLinkPerList.as_view(), name='single_link_in_list'),
   url(r'add-to-list/(?P<list_pk>\d+)/(?P<pk>\d+)$', AddLinkToListView.as_view({'get': 'list'}), name="add"),
   url(r'remove-from-list/(?P<list_pk>\d+)/(?P<pk>\d+)$', RemoveLinkFromListView.as_view(), name="remove"),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

