from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Skill, Education, Wh, Interest

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile_url = serializers.HyperlinkedIdentityField(
        view_name='profile-detail')

    class Meta:
        model = User
        depth = 1
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_staff', 'profile', 'profile_url')

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 1
        model = Skill
        fields = ('url', 'id', 'name', 'skill_type','description')


class InterestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = Interest
        fields = ('url', 'id', 'inte_name', 'description')


#foreign Key serializer
class EducationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model  = Education
        fields = ('url', 'id', 'profile', 'edu_name', 'qualification', 'institute', 'description')

class WhSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model   = Wh
        fields  = ('url', 'id', 'profile', 'work_name', 'title', 'company_name','description')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    user = serializers.ReadOnlyField(source='user.id')
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    # nest serializer
    owned_skills = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Skill.objects.all(),
        view_name='skill-detail'
    )

    education = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name = 'education-detail'

    )

    work_history = serializers.HyperlinkedIdentityField(

        many=True,
        read_only=True,
        view_name='wh-detail'

    )

    chosen_interests  = serializers.HyperlinkedRelatedField(
        many      = True,
        read_only = False,
        queryset  = Interest.objects.all(),
        view_name = 'interest-detail'

    )

    class Meta:
        model = Profile
        depth = 1
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'location', 
                  'about', 'phone', 'birthday', 'linked_in_website', 'twitter_website',
                  'facebook_website','owned_skills','chosen_interests','data_created','date_updated','user','user_url','education','work_history')

    def get_full_name(self, obj):
        request = self.context['request']
        return request.user.get_full_name()
        
        #deal with the nested object by update
    def update(self, instance, validated_data):
        # retrieve the User
        user_data = validated_data.pop('user', None)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        # retrieve Profile
        for attr, value in validated_data.items():
            #put all choosen skills & interests to the list
            if str(attr) == 'owned_skills':
                instance.owned_skills.set(value)

            elif str(attr) == 'chosen_interests':
                instance.chosen_interests.set(value)

            else:
                setattr(instance, attr, value)

        instance.user.save()
        instance.save()
        return instance

