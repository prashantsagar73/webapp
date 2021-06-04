from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets 
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# custom permission 
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricared to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user    


# use viewsets that combine two or multiple class in one 
# automatically create route for every post 
class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()




# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.
# class PostList(generics.ListCreateAPIView):
#     # permission_classes = [IsAdminUser ] #-> only aunthecited admin can see the data api
#     permission_classes = [DjangoModelPermissions] #-> any usr can view and update or add data through api
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     # pass

# # RetrieveDestroyAPIView
# # Used for read or delete endpoints to represent a single model instance.
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission] #-> any usr can view and update or add data through api
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # pass



# for more  option you can go through this site - you can control the api views->like-delelte-create-views
# https://www.django-rest-framework.org/api-guide/generic-views/