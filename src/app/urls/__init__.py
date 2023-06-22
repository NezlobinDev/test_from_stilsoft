from django.contrib import admin
from django.urls import include, path

from app import views as app_views

api = [
    path('v1/', include('app.urls.v1', namespace='v1')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(api)),
    path('summernote/', include('django_summernote.urls')),
    path('', app_views.HomepageView.as_view(), name='homepage'),
]
