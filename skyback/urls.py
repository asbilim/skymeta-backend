from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Skymeta",
      default_version='v1',
      description="Skymeta API documentation",
      terms_of_service="",
      contact=openapi.Contact(email="team@newgenafrica.co"),
      license=openapi.License(name=""),

   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/',include('blog.urls',namespace="")),
    path('documentation<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
