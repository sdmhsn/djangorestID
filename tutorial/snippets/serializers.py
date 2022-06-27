from rest_framework import serializers

from django.contrib.auth.models import User

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    '''
        - ReadOnlyField: only use for serializing and not for deserializing
        - source='owner.username': this argument to refers owner field in models ('auth.User'), by its username field, not by its id field
    '''

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
