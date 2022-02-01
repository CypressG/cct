# Create your views here.
from django.http import HttpResponse
from api.serializers import (
    GroupSerializer,
    RegistrySerializer,
    MeetingSerializer,
    RoomSerializer,
)
from api.models import Group, Registry, Meeting, Room
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOfGroupForGroup, IsOwnerOfGroupForMeeting
import logging


logger = logging.getLogger(__name__)


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logging.info("Started registring Registry object")
        registry = Registry(
            user=self.request.user,
            group=Group.objects.get(pk=serializer.data["id"]),
            is_leader=True,
        )
        logger.info(registry)
        registry.save()
        logger.info(registry)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()


class GroupDetail(generics.RetrieveDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfGroupForGroup]


class RegistryList(generics.ListCreateAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOfGroupForMeeting]


class RegistryDetail(generics.RetrieveDestroyAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOfGroupForMeeting]


class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfGroupForMeeting]


class MeetingDetail(generics.RetrieveDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfGroupForMeeting]


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class RoomDetail(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
