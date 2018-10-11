import django_filters


#from django_filters.widgets import CSVWidget
from jobs.models import Job, Category

class JobFilter(django_filters.FilterSet):
    """
    create filter for class job
    """
    title = django_filters.CharFilter(field_name = 'title', lookup_expr = 'icontains')
    location = django_filters.CharFilter(field_name = 'location', lookup_expr = 'icontains')
    #tag = django_filters.CharFilter(field_name ='tags' , lookup_expr = 'icontains')
    category = django_filters.CharFilter(field_name = 'category__cate_name')



    class Meta:
        model = Job
        fields = ['title','location','category']