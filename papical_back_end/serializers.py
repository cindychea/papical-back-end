from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.hashers import make_password
from papical_back_end.models import User, Hangout, FreeTime, Invitation
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from friendship.models import Friend, FriendshipRequest

import logging
logger = logging.getLogger(__name__)



class UserSerializer(serializers.ModelSerializer):
  
  tag = TagListSerializerField()

  class Meta:
    model = User
    fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'gender', 'location', 'tag', 'picture')

  # validate_password = make_password(password)
  def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


class HangoutSerializer(TaggitSerializer, serializers.ModelSerializer):

  tag = TagListSerializerField()
  creator = serializers.ReadOnlyField(source='creator.username')

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

  class Meta:
    model = Hangout
    fields = ('pk', 'name', 'date', 'start_time', 'end_time', 'description', 'creator', 'location', 'tag')


class FreeTimeSerializer(serializers.ModelSerializer):

  creator = serializers.ReadOnlyField(source='creator.username')
  

  # def perform_create(self, serializer):
  #   creator =  self.context['request'].user
  #   serializer.save(creator=creator)
  #   return creator

  # creator = serializers.HiddenField(default=self.context['request'].user)

  class Meta:
    model = FreeTime
    fields = ('pk', 'date', 'start_time', 'end_time', 'available', 'creator')


class InvitationSerializer(serializers.ModelSerializer):
  creator = serializers.ReadOnlyField(source='creator.username')
  hangout = HangoutSerializer()
  invitee = UserSerializer()

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

  class Meta:
    model = Invitation
    fields = ('pk', 'creator', 'invitee', 'hangout', 'attending')


class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = ('pk', 'name', 'slug')


class FriendSerializer(serializers.ModelSerializer):
  from_user = UserSerializer()
  to_user = UserSerializer()

  class Meta:
    model = Friend
    fields = ('pk', 'to_user', 'from_user', 'created')


class FriendshipRequestSerializer(serializers.ModelSerializer):

  class Meta:
    model = FriendshipRequest
    fields = ('pk', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')
