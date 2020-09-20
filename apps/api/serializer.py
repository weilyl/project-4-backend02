from rest_framework import serializers
from apps.api.models import Link, List, Tag, Review, ListLinks


# referenced relationship first
class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'title', 'notes', 'difficulty')


class TagSerializer(serializers.ModelSerializer):
    link = serializers.ReadOnlyField(source='link.name')

    class Meta:
        model = Tag
        fields = ('id', 'name')


class LinkSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Link
        fields = ('id', 'name', 'description', 'image', 'created_at', 'updated_at',
                  'is_public', 'is_favorite', 'is_saved')
        extra_kwargs = {'links': {'required': False}}
        # https://medium.com/@kingsleytorlowei/building-a-many-to-many-modelled-rest-api-with-django-rest-framework-d41f54fe372


class ListLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListLinks
        fields = ('id', 'list_id', 'link_id')


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # links = LinkSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = List
        fields = ('id', 'name', 'owner', 'description', 'created_at', 'updated_at', 'links')
        extra_kwargs = {'lists': {'required': False}}
