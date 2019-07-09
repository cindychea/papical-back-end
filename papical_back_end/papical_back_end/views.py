from rest_framework import generics
from papical_back_end.models import User, Hangout, Invitation
from papical_back_end.serializers import UserSerializer, HangoutSerializer, InvitationSerializer

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class HangoutList(generics.ListCreateAPIView):
  queryset = Hangout.objects.all()
  serializer_class = HangoutSerializer

class HangoutDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Hangout.objects.all()
  serializer_class = HangoutSerializer


class InvitationList(generics.ListCreateAPIView):
  queryset = Invitation.objects.all()
  serializer_class = InvitationSerializer

class InvitationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Invitation.objects.all()
  serializer_class = InvitationSerializer