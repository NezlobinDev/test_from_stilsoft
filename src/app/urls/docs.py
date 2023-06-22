from django.urls import path, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def get_api_docs_urls(api_version):
    """Generate docs urls for concrete API version."""
    schema_view = get_schema_view(
        openapi.Info(
            title='TestStilsoft API',
            default_version=api_version,
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    return [
        re_path(
            r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json',
        ),
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui',
        ),
        path(
            'redoc/',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc',
        ),
    ]
