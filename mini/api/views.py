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
    aqi = AQI_PROPHET.objects.all().order_by('-id')
    serializer = AQI_PROPHETSerializer(aqi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ALLTEMPLSTMwarangallist(request):
    tempvals=TEMP_LSTM_WARANGAL.objects.all()
    serializer=ALLTEMP_warangal_LSTMSerializer(tempvals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ALLTEMPLSTMkhammamlist(request):
    tempvals=TEMP_LSTM_KHAMMAM.objects.all()
    serializer=ALLTEMP_khammam_LSTMSerializer(tempvals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ALLTEMPLSTMadilabadlist(request):
    tempvals=TEMP_LSTM_ADILABADD.objects.all()
    serializer=ALLTEMP_warangal_LSTMSerializer(tempvals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ALLTEMPLSTMnizamabadlist(request):
    tempvals=TEMP_LSTM_NIZAMABAD.objects.all()
    serializer=ALLTEMP_nizamabad_LSTMSerializer(tempvals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ALLTEMPLSTMkarimnagarlist(request):
    tempvals=TEMP_LSTM_KARIMNAGAR.objects.all()
    serializer=ALLTEMP_karimnagar_LSTMSerializer(tempvals, many=True)
    return Response(serializer.data)

'''
@api_view(['GET'])
districts = ["adilabad","karimnagar","warangal","khammam","nizamabad"]
    readings = AQI_PROPHET.objects.filter(district__in=districts)
'''