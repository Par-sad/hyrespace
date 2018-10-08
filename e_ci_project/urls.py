from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users import views

# import the media path
from django.views.static import serve
from e_ci_project.settings import MEDIA_ROOT

API_TITLE = 'HR API'
API_DESCRIPTION = 'A Web API for creating and viewing jobs and profiles.'

# Create a router and register our viewsets with it.
router = DefaultRouter()
#profile
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'transcripts', views.TranscriptViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'whs', views.WhViewSet)
router.register(r'skill_test', views.SkillTestViewSet)
router.register(r'interests', views.InterestViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    # add jobs urls
    url(r'^', include('jobs.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    # define the file path to url
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

]
