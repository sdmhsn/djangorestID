from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from django.contrib.auth.models import User

from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # IsAuthenticatedOrReadOnly: which will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # save the data owner with request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # to update and delete the snippet, these two permissions class should be True
    '''
        - the IsOwnerOrReadOnly custom permission class is only able to GET, PUT and DELETE methods. we don't want any user have 
        permission to update (PUT) or delete (DELETE) our own snippet. they only can read (GET) our snippet
    '''


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
