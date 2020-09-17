from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics  # contains filters so spec categories belong to spec users
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Link, List, Tag, Review
from apps.api.serializer import LinkSerializer, ListSerializer, TagSerializer, ReviewSerializer


class ListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = List.objects.all().filter(
            owner=self.request.user
        )
        return queryset

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


class ListLinks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        if self.kwargs.get('list_pk'):
            user_list = List.objects.get(pk=self.kwargs['list_pk'])
            queryset = Link.objects.filter(
                owner=self.request.user,
                list=user_list,
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    class SingleLinkPerList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        if self.kwargs.get('list_pk') and self.kwargs.get('pk'):
            user_list = List.objects.get(pk=self.kwargs['list_pk'])
            queryset = Link.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                list=user_list
            )
            return queryset


class LinksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.all().filter(
            user_list=List.objects.filter(owner=self.request.user)
        )
        return queryset
