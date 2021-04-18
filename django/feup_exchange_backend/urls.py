from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

from .views import TestServiceView

# # -- Load Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="FEUP Exchange REST API",
        default_version='v1',
        description="Swagger web platform that can be used to access the "
                    "FEUP Exchange REST API endpoints."
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
    url=os.environ.get("SWAGGER_BASE_URL", default=None)
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/?$', schema_view.with_ui('swagger',
                                                cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/?$', schema_view.with_ui('redoc',
                                              cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^test/?$', TestServiceView.as_view(), name="test")
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
