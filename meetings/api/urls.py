from django.urls import path
from . import views

# from rest_framework import permissions

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "api"

# Main API URL paths
urlpatterns = [
    path("groups/", views.GroupList.as_view(), name="group"),
    path("groups/<int:pk>", views.GroupDetail.as_view(), name="group-detail"),
    path("meetings/", views.MeetingList.as_view(), name="meeting"),
    path(
        "meetings/<int:pk>",
        views.MeetingDetail.as_view(),
        name="meeting-detail",
    ),
    path("registries/", views.RegistryList.as_view(), name="registry"),
    path(
        "registries/<int:pk>",
        views.RegistryDetail.as_view(),
        name="registry-detail",
    ),
    path("rooms/", views.RoomList.as_view(), name="room"),
    path("rooms/<int:pk>", views.RoomDetail.as_view(), name="room-detail"),
]


# Swagger additional URL paths
urlpatterns += (
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI:
    path(
        "",  # schema/swagger-ui afterwards
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc",
    ),
)
