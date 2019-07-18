from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import AllowAny
from papical_back_end.permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response
from papical_back_end.models import User, Hangout, FreeTime, Invitation
from taggit_serializer.serializers import TaggitSerializer
from taggit.models import Tag
from friendship.models import Friend, FriendshipRequest
from papical_back_end.serializers import UserSerializer, HangoutSerializer, FreeTimeSerializer, InvitationSerializer, TagSerializer, FriendSerializer, FriendshipRequestSerializer
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  permission_classes = (permissions.IsAuthenticated,)

  def get_permissions(self):
    if self.request.method == 'POST':
      self.permission_classes = (AllowAny,)
    return super(UserViewSet, self).get_permissions()
  
  def list(self, request):
    queryset = User.objects.filter(Q(username=request.user.username)).all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

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
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated,)
  
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
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated,)

  # def get_serializer_context(self):
  #   """
  #   pass request attribute to serializer
  #   """
  #   context = super(FreeTimeViewSet, self).get_serializer_context()
  #   return context

  # def perform_create(self, serializer):
  #   serializer.save(creator=self.request.user)

  # def get_serializer_context(self):
  #   return {'request': self.request}

  
  # def list(self, request):
  #   # List
  #   pass

  # def create(self, request):

  # #   creator =  self.context['request'].user
  # #   serializer.save(creator=creator)
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
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated,)
  
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
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated,)
  
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


# Rework FriendViewSet with more generic ViewSet to allow for alignment with library
class FriendViewSet(viewsets.ModelViewSet):
  serializer_class = FriendSerializer
  queryset = Friend.objects.all()
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated, )
  
  def list(self, request):
    queryset = Friend.objects.filter(Q(from_user=request.user) | Q(to_user=request.user)).all()
    serializer = FriendSerializer(queryset, many=True)
    return Response(serializer.data)

  def destroy(self, request, pk=None):
    friendship = Friend.objects.get(pk=pk)
    friendship.delete()
    return Response({'status': 'Request deleted'}, status=200)


class FriendRequestViewSet(viewsets.ModelViewSet):
  serializer_class = FriendshipRequestSerializer
  queryset = FriendshipRequest.objects.all()
  permission_classes = (permissions.AllowAny, )
  # permission_classes = (permissions.IsAuthenticated, )

  def list(self, request):
    queryset = FriendshipRequest.objects.filter(Q(from_user=request.user) | Q(to_user=request.user)).all()
    serializer = FriendshipRequestSerializer(queryset, many=True)
    return Response(serializer.data)

  def create(self, request):
    # to_user = user_model.objects.get(username=to_username)
    to_user = "" # get id from request params or url path
    Friend.objects.add_friend(request.user, to_user)
    # serializer = FriendshipRequestSerializer(queryset, many=True)
    return Response({'status': 'Request sent'}, status=200)

  def retrieve(self, request, pk=None):
    queryset = FriendshipRequest.objects.get(pk=pk)
    serializer = FriendshipRequestSerializer(queryset, many=False)
    return Response(serializer.data)

  def update(self, request, pk=None):
    friendship = FriendshipRequest.objects.get(pk=pk)

    answer = request.data["answer"]
    
    # {
    #   "accepted": friendship.accept,
    #   "rejected": friendship.reject
    # }.get(answer)()

    if answer == "accepted":
      friendship.accept()
      return Response({'status': 'Request accepted'}, status=200)
    elif answer == "rejected":
      friendship.reject()
      return Response({'status': 'Request rejected'}, status=200)

  def destroy(self, request, pk=None):
    friendship = FriendshipRequest.objects.get(pk=pk)
    friendship.cancel()
    return Response({'status': 'Request deleted'}, status=200)
