from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    # allow user to auth through restframework page 
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
