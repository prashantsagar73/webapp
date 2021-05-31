from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions

# custom permission 
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricared to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user    


# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.
class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser ] #-> only aunthecited admin can see the data api
    permission_classes = [DjangoModelPermissions] #-> any usr can view and update or add data through api
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    # pass

# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission] #-> any usr can view and update or add data through api
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pass



# for more  option you can go through this site - you can control the api views->like-delelte-create-views
# https://www.django-rest-framework.org/api-guide/generic-views/