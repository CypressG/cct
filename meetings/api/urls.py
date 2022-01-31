from django.urls import path
from . import views

# from rest_framework import permissions

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [
    # path("/", views.index, name="index"),
    path("groups/", views.GroupList.as_view(), name="group"),
    path("groups/<int:pk>", views.GroupDetail.as_view(), name="group-item"),
]


# Swagger additional url paths
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
