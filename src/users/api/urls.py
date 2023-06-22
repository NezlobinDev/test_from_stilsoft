from django.urls import include, path

from rest_framework.routers import DefaultRouter

from users.api.views import RegAuthViewSet, UserDataViewSet

router = DefaultRouter()
router.register('', RegAuthViewSet, basename='reg_auth_users')
router.register(r'(?P<uid>\d+)', UserDataViewSet, basename='user_data')

urlpatterns = [
    path('', include(router.urls)),
]
