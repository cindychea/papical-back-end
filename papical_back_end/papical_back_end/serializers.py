from rest_framework import serializers
from papical_back_end.models import User, Hangout, Invitation
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from friendship.models import Friend


class UserSerializer(TaggitSerializer, serializers.ModelSerializer):

  tag = TagListSerializerField()

  class Meta:
    model = User
    fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'location', 'tag')


class HangoutSerializer(TaggitSerializer, serializers.ModelSerializer):

  tag = TagListSerializerField()
  creator = serializers.ReadOnlyField(source='creator.username')

  class Meta:
    model = Hangout
    fields = ('pk', 'name', 'date', 'start_time', 'end_time', 'description', 'creator', 'location', 'tag')


class InvitationSerializer(serializers.ModelSerializer):

  creator = serializers.ReadOnlyField(source='creator.username')

  class Meta:
    model = Invitation
    fields = ('pk', 'creator', 'invitee', 'hangout', 'attending')

class TagSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tag
    fields = ('pk', 'name', 'slug')

class FriendSerializer(serializers.ModelSerializer):

  class Meta:
    model = Friend
    fields = ('pk', 'to_user', 'from_user', 'created')