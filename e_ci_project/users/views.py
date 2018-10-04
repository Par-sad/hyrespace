from rest_framework import viewsets, mixins, permissions
from django.contrib.auth.models import User
<<<<<<< HEAD
from users.models import Profile, Skill, Transcript
from users.serializers import UserSerializer, ProfileSerializer, SkillSerializer, TranscriptSerializer
=======
from users.models import Profile, Skill, Education,Wh,Interest
from users.serializers import UserSerializer, ProfileSerializer, SkillSerializer, EducationSerializer,WhSerializer, InterestSerializer
>>>>>>> hyrespace/ForeignKey_002
from users.permissions import (
    IsOwnerOrReadOnly, IsAdminUserOrReadOnly, IsSameUserAllowEditionOrReadOnly
)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsSameUserAllowEditionOrReadOnly,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class SkillViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)

<<<<<<< HEAD
class TranscriptViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)
=======

class EducationViewSet(viewsets.ModelViewSet):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)


class WhViewSet(viewsets.ModelViewSet):

    queryset = Wh.objects.all()
    serializer_class = WhSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)


class InterestViewSet(viewsets.ModelViewSet):


    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminUserOrReadOnly)
>>>>>>> hyrespace/ForeignKey_002
