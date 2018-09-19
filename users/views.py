from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .serializers import ProfileSerializer
from .models import UserProfile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    @detail_route()
    def changeTitle(self, request, *args, **kwargs):
        get = request.GET
        UserProfile = self.get_object()
        UserProfile.title = get.get('newTitle')
        UserProfile.save()

        return Response(UserProfile.title)
