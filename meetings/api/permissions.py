from rest_framework import permissions
from api.models import Registry, Group
from django.core.exceptions import ObjectDoesNotExist

import logging

logger = logging.getLogger(__name__)


class IsOwnerOfGroupForGroup(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method == "DELETE":
            logger.info("Trying to perform a DELETE http request")
            try:
                Registry.objects.get(
                    user=request.user,
                    is_leader=True,
                    group=Group.objects.get(pk=obj.id),
                )
                logger.info(
                    f"{request.user} tried - Object did indeed existed"
                )
                return True
            except ObjectDoesNotExist:
                logger.error(
                    f"{request.user} tried DELETE on an {obj.name} - Object did not existed. "
                )
                return False
        logger.info(f"{request.user} did infact used safe method")
        return request.method in permissions.SAFE_METHODS


class IsOwnerOfGroupForMeeting(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "POST":
                logger.info(f"{request.user} is trying to send POST request")
                try:

                    Registry.objects.get(
                        user=request.user,
                        group=Group.objects.get(pk=request.data["group"]),
                        is_leader=True,
                    )
                    logger.info(
                        f"{request.user} did accomplished a permission level access to POST request"
                    )
                    return True
                except ObjectDoesNotExist:
                    logger.error(
                        f"{request.user} did not found the objects in the Registry so is not given an permission to post"
                    )
                    return False
        except KeyError:
            logger.error(
                f"{request.user} tried accessing page and did not succeed because of the KeyError"
            )
            return True
        return request.method in permissions.SAFE_METHODS
