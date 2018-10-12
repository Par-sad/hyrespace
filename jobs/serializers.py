from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


from .models import Company,Category,Job


# tag serializer


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
        fields = ('url','id','status','company','title','description','tags','location','category','start_date',
                  'due_date','date_add', 'date_updated')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(JobSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance


    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start_date'] > data['due_date']:
            raise serializers.ValidationError("finish must occur after start")
        return data