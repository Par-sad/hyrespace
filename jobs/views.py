from rest_framework import viewsets, mixins, permissions
#from django.contrib.auth.models import User
from jobs.models import Company,Category,Job
from jobs.serializers import CompanySerializer,CategorySerializer,JobSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

#to finally save the tags to the previously saved Job-model.
