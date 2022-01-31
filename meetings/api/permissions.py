from rest_framework import permissions
from api.models import Registry, Group
from django.core.exceptions import ObjectDoesNotExist


class IsOwnerOfGroup(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "DELETE":
            try:
                Registry.objects.get(
                    user=request.user,
                    is_leader=True,
                    group=Group.objects.get(pk=obj.id),
                )
                return True
            except ObjectDoesNotExist:
                return False
