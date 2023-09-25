from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: index')
    return HttpResponse('<h2>Домашнее задание к семинару 2</h2>')
# Create your views here.
