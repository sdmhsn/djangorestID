from rest_framework import serializers

from django.contrib.auth.models import User

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    '''
        - ReadOnlyField: only use for serializing and not for deserializing
        - source='owner.username': this argument to refers owner field in models ('auth.User'), by its username field, not by its id field
    '''
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())  # PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']  # 'snippets': it refers to reverse relationship between User model and Snippet model (related_name='snippets' in owner field)
