from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

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


# fbv for root endpoint of our API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),  # the reverse() function drf, in order to return fully-qualified URLs.
        'snippets': reverse('snippet-list', request=request, format=format)
    })

# cbv for root endpoint of our API
# class ApiRoot(generics.GenericAPIView):
#     def get(self, request, format=None):
#         return Response({
#             'users': reverse('user-list', request=request, format=format),
#             'snippets': reverse('snippet-list', request=request, format=format)
#         })


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()  # .get_object(): base method in GenericAPIView. Returns an object instance that should be used for detail views.
        # print(snippet)
        # print(snippet.highlighted)
        return Response(snippet.highlighted)  # only return the highlighted field in an object instance Snippet model
