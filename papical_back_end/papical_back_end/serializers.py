from rest_framework import serializers
from papical_back_end.models import User, Hangout, Invitation
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class UserSerializer(TaggitSerializer, serializers.ModelSerializer):
  
  tag = TagListSerializerField()

  class Meta:
    model = User
    fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'location', 'tag')


class HangoutSerializer(TaggitSerializer, serializers.ModelSerializer):
  
  tag = TagListSerializerField()

  class Meta:
    model = Hangout
    fields = ('pk', 'name', 'date', 'start_time', 'end_time', 'description', 'creator', 'location', 'tag')


class InvitationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Invitation
    fields = ('pk', 'invitee', 'hangout', 'attending')

class TagSerializer(serializers.ModelSerializer):

  # tag = TagListSerializerField()

  class Meta:
    model = Tag
    fields = ('pk', 'name', 'slug')
