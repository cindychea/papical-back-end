from rest_framework import serializers
from papical_back_end.models import User, UserProfile, Hangout, FreeTime, Invitation
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from friendship.models import Friend, FriendshipRequest


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'location', 'tag', 'picture')

class UserProfileSerializer(TaggitSerializer, serializers.ModelSerializer):

  tag = TagListSerializerField()

  class Meta:
    model = UserProfile
    fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'location', 'tag', 'picture')

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

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

  class Meta:
    model = FreeTime
    fields = ('pk', 'date', 'start_time', 'end_time', 'available', 'creator')


class InvitationSerializer(serializers.ModelSerializer):

  creator = serializers.ReadOnlyField(source='creator.username')

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



    # {
    #   pk: 2,
    #   message: "adsfasdfasdf",
    #   created: "",
    #   rejected: "",
    #   from_user: {
    #     id: 1,
    #     name: "Jasmin",
    #     email: "asdfasd@#adsfadsf"
    #   },
    #   to_user: {
    #     id: 2,
    #     name: "Cindy",
    #     email: "asdfasd@#adsfadsf"
    #   },
    # }

