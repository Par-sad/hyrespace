from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import Profile, Skill, OwnedSkills, Transcript
=======
from .models import Profile, Skill, Education, Wh, Interest
>>>>>>> hyrespace/ForeignKey_002

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

<<<<<<< HEAD
class TranscriptSerializer(serializers.HyperlinkedModelSerializer):
    profile_url = serializers.HyperlinkedIdentityField(view_name='profile-detail')
    profile = serializers.ReadOnlyField(source='profile.id')
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        depth = 1
        model = Transcript
        fields = "__all__"
=======

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

>>>>>>> hyrespace/ForeignKey_002

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    user = serializers.ReadOnlyField(source='user.id')
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
<<<<<<< HEAD
    #skill foreign key
=======
    # nest serializer
>>>>>>> hyrespace/ForeignKey_002
    owned_skills = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Skill.objects.all(),
        view_name='skill-detail'
    )
    #transcript foreign key
    transcripts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Transcript.objects.all(),
        view_name='transcript-detail'
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
<<<<<<< HEAD
                  'about', 'phone', 'birthday', 'image', 'linked_in_website', 'twitter_website',
                  'facebook_website','owned_skills','date_created','date_updated','user','user_url', 'transcripts')
=======
                  'about', 'phone', 'birthday', 'linked_in_website', 'twitter_website',
                  'facebook_website','owned_skills','chosen_interests','data_created','date_updated','user','user_url','education','work_history')
>>>>>>> hyrespace/ForeignKey_002

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
<<<<<<< HEAD
            if str(attr) != 'owned_skills' and str(attr) != 'transcripts':
                setattr(instance, attr, value)
            elif str(attr) == 'owned_skills':
        #put all choosen skills to the list
                    instance.owned_skills.set(value)
            else:
                instance.transcripts.set(value)
=======
            #put all choosen skills & interests to the list
            if str(attr) == 'owned_skills':
                instance.owned_skills.set(value)

            elif str(attr) == 'chosen_interests':
                instance.chosen_interests.set(value)

            else:
                setattr(instance, attr, value)

>>>>>>> hyrespace/ForeignKey_002
        instance.user.save()
        instance.save()
        return instance

<<<<<<< HEAD
    def create(self, validated_data):
        transcripts_data = validated_data.pop('transcripts')
        profile = Profile.objects.create(**transcripts_data)
        for transcript_data in transcripts_data:
            Transcript.objects.create(profile=profile, **transcript_data)
        return profile



=======
>>>>>>> hyrespace/ForeignKey_002
