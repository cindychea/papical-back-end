from rest_framework import generics, permissions
from papical_back_end.models import User, Hangout, Invitation
from taggit_serializer.serializers import TaggitSerializer
from taggit.models import Tag
from friendship.models import Friend
from papical_back_end.serializers import UserSerializer, HangoutSerializer, InvitationSerializer, TagSerializer, FriendSerializer

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

class FriendList(generics.ListCreateAPIView):
  queryset = Friend.objects.all()
  serializer_class = FriendSerializer
  permission_classes = (permissions.IsAuthenticated,)

class FriendDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Friend.objects.all()
  serializer_class = FriendSerializer
  permission_classes = (permissions.IsAuthenticated,)
