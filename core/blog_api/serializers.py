# serializer->is a trasnslator| converter  for other frameworks to django database 

from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','category','published','title','slug' , 'author', 'excerpt', 'content','status')

