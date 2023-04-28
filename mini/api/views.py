from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from api.serializers import *

import datetime

# Create your views here.

@api_view(['GET'])
def AQI_PROPHETlist(request):
    books = AQI_PROPHET.objects.all().order_by('-id')
    serializer = AQI_PROPHETSerializer(books, many=True)
    return Response(serializer.data)

