import djongo
import json, time
import pymongo
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from datetime import datetime

@api_view(['GET'])
def ping(request):
    if request.method == 'GET':
        return JsonResponse({
            "message" : "ok"
        })