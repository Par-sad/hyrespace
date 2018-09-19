from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from django.urls import include, path
from users import views

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
