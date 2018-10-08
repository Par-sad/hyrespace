from rest_framework import serializers
#from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Company,Category,Job



class CompanySerializer(serializers.HyperlinkedModelSerializer):

#foreign key
    job = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name = 'job-detail'

    )

    class Meta:

        model = Company
        fields = ('url','id','name','telephone','fax','address','date_add','job')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Category
        fields = ('url', 'id', 'cate_name' )

# serialize the tag, gain control over the serialization


class JobSerializer(TaggitSerializer,serializers.HyperlinkedModelSerializer):

    #foreign key
    category = serializers.HyperlinkedRelatedField(

        many=True,
        read_only=False,
        queryset =Category.objects.all(),
        view_name = 'category-detail'

    )


    # tag serializer
    tags = TagListSerializerField()

    class Meta:
        model = Job
        fields = ('url','id','company','title','description','tags','location','category','start_date',
                  'due_date','date_add', 'date_updated')

