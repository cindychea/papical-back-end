from rest_framework import generics, permissions
from papical_back_end.models import User, Hangout, Invitation
from taggit_serializer.serializers import TaggitSerializer
from taggit.models import Tag
from papical_back_end.serializers import UserSerializer, HangoutSerializer, InvitationSerializer, TagSerializer

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class HangoutList(generics.ListCreateAPIView):
  queryset = Hangout.objects.all()
  serializer_class = HangoutSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

class HangoutDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Hangout.objects.all()
  serializer_class = HangoutSerializer
  permission_classes = (permissions.IsAuthenticated,)


class InvitationList(generics.ListCreateAPIView):
  queryset = Invitation.objects.all()
  serializer_class = InvitationSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

class InvitationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Invitation.objects.all()
  serializer_class = InvitationSerializer
  permission_classes = (permissions.IsAuthenticated,)


class TagList(generics.ListCreateAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  permission_classes = (permissions.IsAuthenticated,)

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  permission_classes = (permissions.IsAuthenticated,)
