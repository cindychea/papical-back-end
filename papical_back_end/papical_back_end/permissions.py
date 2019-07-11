from rest_framework import permissions

# Users can view their own profile and those of their friends

# Users can see hangouts they created or hangouts they are invited to
class IsHangoutCreatorOrInvited(permissions.BasePermission):
  message = 'No access to this hangout.'

  def has_object_permission(self, request, view, obj):
    return request.user == obj.creator or request.user == obj.invitations.invitee

# Users can see invitations they created or invitations sent to them
class IsInvitationCreatorOrInvitee(permissions.BasePermission):
  message = 'No access to this invitation.'

  def has_object_permission(self, request, view, obj):
    return request.user == obj.creator or request.user == obj.invitee

# No restrictions on tags

# Users can see their friends/requests/etc. 
