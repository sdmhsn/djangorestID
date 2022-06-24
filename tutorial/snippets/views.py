from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):  # GenericAPIView extends Rest framework's APIView
    queryset = Snippet.objects.all()  # GenericAPIView attributes
    serializer_class = SnippetSerializer  # GenericAPIView attributes

    '''
        by adding queryset and serializer_class above, now the .get()
        and .post() methods that we are binding below, already have
        queryset (returning objects) and serializer (serializing output
        and deserializing input)
    '''

    def get(self, request, *args, **kwargs):  # explicitly binding the get() from APIView
        return self.list(request, *args, **kwargs)  # .list(): ListModelMixin method

    def post(self, request, *args, **kwargs):  # explicitly binding the post() from APIView
        return self.create(request, *args, **kwargs)  # .create(): CreateModelMixin method


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # .retrieve(): RetrieveModelMixin method

    def put(self, request, *args, **kwargs):  # explicitly binding the put() from APIView
        return self.update(request, *args, **kwargs)  # .update(): UpdateModelMixin method

    def delete(self, request, *args, **kwargs):  # explicitly binding the delete() from APIView
        return self.destroy(request, *args, **kwargs)  # .retrieve(): DestroyModelMixin method
