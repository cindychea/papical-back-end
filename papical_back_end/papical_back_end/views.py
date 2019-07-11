from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from papical_back_end.models import User, Hangout, FreeTime, Invitation
from taggit_serializer.serializers import TaggitSerializer
from taggit.models import Tag
from friendship.models import Friend, FriendshipRequest
from papical_back_end.serializers import UserSerializer, HangoutSerializer, FreeTimeSerializer, InvitationSerializer, TagSerializer, FriendSerializer, FriendshipRequestSerializer

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
  #   queryset = Friend.objects.select_related("from_user", "to_user").filter(to_user=request.user).all()
  #   serializer = FriendSerializer(queryset, many=True)
  #   return Response(serializer.data)

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
  #   Friend.objects.remove_friend(request.user, to_user)

  #   return Response({'status': 'Request deleted'}, status=200)


class FriendRequestViewSet(viewsets.ModelViewSet):
  serializer_class = FriendshipRequestSerializer
  queryset = FriendshipRequest.objects.all()
  permission_classes = (permissions.IsAuthenticated, )

  def list(self, request):
    queryset = FriendshipRequest.objects.select_related("from_user", "to_user").filter(to_user=request.user).all()
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












  # def list(self, request):
  #   queryset = Friend.objects.all()
  #   serializer = FriendSerializer(queryset, many=True)
  #   return Response(serializer.data)

  # @action(detail=True, methods=['get'])
  # def list_requests(self, request, pk=None):
  #   queryset = Friend.objects.unread_requests(request.user)
  #   serializer = FriendSerializer(queryset, many=True)
  #   return Response(serializer.data)

  # @action(detail=True, methods=['post'])
  # def make_request(self, request, pk=None):
  #   other_user = User.objects.get(pk=1)
  #   serializer = FriendSerializer(data=request.data)

  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data)
  #   return Response(serializer.errors)



  # https://github.com/revsys/django-friendship/blob/master/friendship/views.py