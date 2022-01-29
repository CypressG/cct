from django.urls import path, re_path
from . import views
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [path("", views.index, name="index")]


# Swagger additional url paths
urlpatterns += (
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc",
    ),
)
