from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug("Attempting to connect to not configured url. ")

    return HttpResponse("<h1>Page not found </h1>", status=404)
