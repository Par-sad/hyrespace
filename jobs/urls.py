from jobs import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.

#jobs
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'companies',views.CompanyViewSet)
router.register(r'jobs',views.JobViewSet)
router.register(r'categories',views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
