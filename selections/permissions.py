from django.http import Http404
from rest_framework.permissions import BasePermission


from selections.models import Selection


# class IsOwner(permissions.BasePermission):
#     message = "No Permissions"
#
#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated
#
#     def has_object_permission(self, request, view, obj):
#         if hasattr(obj, "owner"):
#             return (request.user and request.user.is_authenticated and obj.owner == request.user) or (
#                 request.user.is_staff)
#         else:
#             return False


class SelectionEditPermission(BasePermission):
    message = "You can only edit your selections"

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise Http404

        if selection.owner_id == request.user.id:
            return True
        return False
