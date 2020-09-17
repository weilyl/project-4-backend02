from rest_framework import serializers
from apps.api.models import Link, List


# referenced relationship first
class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Link
        fields = ('id', 'list', 'name', 'description', 'created_at', 'updated_at',
                  'is_public', 'is_favorite', 'is_saved')


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    links = LinkSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = List
        fields = ('id', 'name', 'owner', 'description', 'created_at', 'updated_at')

