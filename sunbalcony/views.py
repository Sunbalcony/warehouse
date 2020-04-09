from django.shortcuts import render
from django.http import HttpResponse
import json
import requests


# from . import models

def index(request):
    return HttpResponse("Hello world ! ")
