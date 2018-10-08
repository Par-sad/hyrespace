from rest_framework import serializers
#from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

import six

from .models import Company,Category,Job



# tag serializer
class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)
        return value


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
    tags = NewTagListSerializerField()

    class Meta:
        model = Job
        fields = ('url','id','status','company','title','description','tags','location','category','start_date',
                  'due_date','date_add', 'date_updated')

