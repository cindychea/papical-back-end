from rest_framework import generics, permissions, viewsets
from papical_back_end.models import User, Hangout, FreeTime, Invitation
from taggit_serializer.serializers import TaggitSerializer
from taggit.models import Tag
from friendship.models import Friend
from papical_back_end.serializers import UserSerializer, HangoutSerializer, FreeTimeSerializer, InvitationSerializer, TagSerializer, FriendSerializer

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass



class HangoutViewSet(viewsets.ModelViewSet):
  serializer_class = HangoutSerializer
  queryset = Hangout.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass



class FreeTimeViewSet(viewsets.ModelViewSet):
  serializer_class = FreeTimeSerializer
  queryset = FreeTime.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass



class InvitationViewSet(viewsets.ModelViewSet):
  serializer_class = InvitationSerializer
  queryset = Invitation.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass



class TagViewSet(viewsets.ModelViewSet):
  serializer_class = TagSerializer
  queryset = Tag.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass



class FriendViewSet(viewsets.ModelViewSet):
  serializer_class = FriendSerializer
  queryset = Friend.objects.all()
  permission_classes = (permissions.IsAuthenticated,)
  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   # Detail
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass
