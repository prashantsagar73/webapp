from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
# this will provide usrinterface for API documentation
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # webpp url 
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    # blog api for react
    path('api/', include('blog_api.urls', namespace='blog_api')),
    # user management 
    path ('api/user/',include('users.urls',namespace='users')),
    # schema 
    path('docs', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title= "BlogApi",
        description = "API for the BlogAPI",
        version = "1.0.0",
    ),    name = "openapi-schema" ),

]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
