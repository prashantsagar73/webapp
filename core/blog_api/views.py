from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    # pass

# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pass



# for more  option you can go through this site - you can control the api views->like-delelte-create-views
# https://www.django-rest-framework.org/api-guide/generic-views/