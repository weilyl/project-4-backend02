from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics  # contains filters so spec categories belong to spec users
from rest_framework import viewsets
from django.views.generic import View
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Link, List, Tag, Review
from apps.api.models import ListLinks as Membership
from apps.api.serializer import LinkSerializer, ListSerializer, TagSerializer, ReviewSerializer, ListLinksSerializer


# Get all lists, create lists, delete lists; how to use perform_destroy to ask before deleting?
# Only specific user can do this
class ListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    # returns all links created by user
    def get_queryset(self):
        queryset = List.objects.all().filter(
            owner=self.request.user
        )
        return queryset

    # create new list
    def create(self, request, *args, **kwargs):
        user_list = List.objects.filter(
            name=request.data.get('name'),
            owner=request.user,
        )
        if user_list:
            msg = 'You already have a list with that name. Do you want to add to that list instead?'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        pass

    # delete list if owned by user
    def destroy(self, request, *args, **kwargs):
        user_list = List.objects.get(pk=self.kwargs['pk'])
        if not request.user == user_list.owner:
            raise PermissionDenied("You don't have permission to delete this list")
        super().destroy(request, *args, **kwargs)
        return Response(
            {
                'message': f'{user_list} has been deleted',
                'status': status.HTTP_200_OK
            }
        )

    # edit existing list if owned by user
    def update(self, request, *args, **kwargs):
        user_list = List.objects.filter(pk=self.kwargs["pk"]).first()
        print(user_list)
        print(user_list.owner)
        if not request.user == user_list.owner:
            raise PermissionDenied(
                "You have no permissions to edit this recipe"
            )
        else:
            List.objects.filter(pk=self.kwargs["pk"]).update()
        return super().update(request, **kwargs)


# Get all links in a specific list
# Add links for a specific list?  What does perform create do?
class ListLinksViewSet(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    # get all links from list
    # NEED TO TEST AGAIN once method to add link to list is working
    def get_queryset(self):
        if self.kwargs.get('list_pk'):
            user_list = List.objects.get(pk=self.kwargs['list_pk'])
            # queryset = Link.objects.filter(
            #     owner=self.request.user,
            # )
            user_links = []
            for link_id in user_list.links.all():
                user_link_singular = Link.objects.get(pk=link_id['id']).first()
                user_links.append(user_link_singular)
            return user_links

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Get one link on a specific list
# post-MVP edit/add/delete tags for a specific link on a specific list
# How to add/remove links from list without removing links from website:
# http://www.learningaboutelectronics.com/Articles/How-to-add-or-remove-an-object-ManyToManyField-in-Django.php
class SingleLinkPerList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    # NEED TO FIX to get one link from one list; may not need for MVP?
    # def get_queryset(self):
    #     if self.kwargs.get('list_pk') and self.kwargs.get('pk'):
    #         queryset = Link.objects.filter(
    #             pk=self.kwargs['pk'],
    #         )
    #         user_list = List.objects.filter(
    #             pk=self.kwargs['list_pk'],
    #             owner=self.request.user,
    #         )
    #         return user_list
    def get_queryset(self):
        if self.kwargs.get('list_pk') and self.kwargs.get('pk'):
            queryset = List.links.through.objects.filter(
                pk=self.kwargs['pk'],
            )
            user_list = List.objects.filter(
                pk=self.kwargs['list_pk'],
                owner=self.request.user,
            )
            return queryset


class RemoveLinkFromListView(View):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    # take one link from list without deleting from database; remove relation between link and list
    # NEED TO FIX
    # NEED TO TEST AFTER MAKING CREATE COUNTERPART
    # maybe I can take this destroy & its create counterpart out of class & make custom routes so I don't need request methods??
    def get(self):
        if self.request.method == 'GET':
            if self.kwargs.get('list_pk') and self.kwargs.get('pk'):
                user_list = List.objects.get(pk=self.kwargs['list_pk'])
                queryset = Link.objects.get(
                    pk=self.kwargs['pk'],
                    # owner=self.request.user,
                    # list=user_list
                )
                user_list.links.remove(queryset)
                user_list.save()
                # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/many_to_many.html
                # even though other resources says .save() is not necessary for m2m
                return user_list.links.all()
            else:
                raise ValidationError(
                    "Link could not be removed"
                )


class AddLinkToListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListLinksSerializer

    # @api_view(('GET',))
    # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    # NEED TO FIX
    # add link to list; add relation to many to many field 'links' in list object
    # def get(self, request, **kwargs):
    #     # if self.request.method == 'GET':
    #     print("This is a GET method")
    #     if self.kwargs.get('list_pk') and self.kwargs.get('pk'):
    #         user_list = List.objects.get(pk=self.kwargs['list_pk'])
    #         # user_list.links.append('pk')
    #         # print(Link(user_list['id']))
    #         user_link = Link.objects.get(pk=self.kwargs['pk'])
    #         print(user_link)
    #         user_list.links.add(user_link.id)
    #         # user_list.links.append('pk')
    #         user_list.save()
    #         print(user_list)
    #         data = {'count': queryset.count()}
    #         return Response(data, template_name='assessments.html')
    #         # return Response(
    #         #     {
    #         #         "message": f'{user_list.links}',
    #         #         "status": status.HTTP_200_OK
    #         #     }
    #         # )
    #     else:
    #         raise ValidationError(
    #             "Link could not be added"
    #         )
    def get_queryset(self):
        print(self.request.user)
        print(self.kwargs['pk'])
        print(self.kwargs['list_pk'])
        pk1 = self.kwargs['list_pk']
        pk2 = self.kwargs['pk']
        user_list = List.objects.get(pk=pk1)
        print(user_list)
        user_link = Link.objects.get(pk=pk2)
        print(user_link)
        # user_list.links.append(user_link.id)
        # tied = ListLinks(list_id=user_list, link_id=user_link)
        # tied = Membership.objects.create(list_id=user_list, link_id=user_link)
        tied = Membership.objects.create(list_id=user_list, link_id=user_link)
        print(tied)
        tied.save()
        # return List.objects.filter(pk=pk1).values()
        return Membership.objects.values()


# Get all links saved by a specific user
# should I change 'is_saved' property for a link when it's created and/or added to a list?
class LinksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    # def get_queryset(self):
    #     # queryset = Link.objects.all().filter(
    #     #     user_list=List.objects.filter(owner=self.request.user)
    #     # )
    #     # list.links.added.all
    #     # set attribute added on link model to find all lists a link has be added to
    #     queryset = List.objects.filter(owner=self.request.user)
    #     all_links = []
    #     for user_list in queryset:
    #         print(user_list)
    #         user_links = user_list.links.all()
    #         print(user_links)
    #         for user_link in user_links:
    #             print(user_link)
    #             if user_link in all_links:
    #                 pass
    #             else:
    #                 print(all_links)
    #                 return user_link
    #             print(all_links)
    #             all_links.append(user_link)
    #     print(all_links)
    #     # 2020-09-18 11:40pm: prints have shown that both lists are named Scarves02 & do not have related lists
    #     return all_links

    # return all links in database
    def get_queryset(self):
        queryset = Link.objects.all()
        return queryset

    def get(self):
        user_link = Link.objects.get(pk=self.kwargs['pk'])
        return user_link

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Please make an account to add a link to our database"
            )
        return super().create(request, *args, **kwargs)
