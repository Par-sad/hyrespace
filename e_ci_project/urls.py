from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'skills', views.SkillViewSet)

router.register(r'educations', views.EducationViewSet)
router.register(r'whs', views.WhViewSet)
router.register(r'interests', views.InterestViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token, name='api-token-auth')
]
