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

@api_view(['GET'])
def AQIPhrophetadilabad(request):
    values=AQI_PROPHET.objects.filter(district="adilabad")
    serializer=AQI_PROPHETSerializer(values,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AQIPhrophetkarimnagar(request):
    values=AQI_PROPHET.objects.filter(district="karimnagar")
    serializer=AQI_PROPHETSerializer(values,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AQIPhrophetkhammam(request):
    values=AQI_PROPHET.objects.filter(district="khammam")
    serializer=AQI_PROPHETSerializer(values,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AQIPhrophetwarangal(request):
    values=AQI_PROPHET.objects.filter(district="warangal")
    serializer=AQI_PROPHETSerializer(values,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AQIPhrophetnizamabad(request):
    values=AQI_PROPHET.objects.filter(district="nizamabad")
    serializer=AQI_PROPHETSerializer(values,many=True)
    return Response(serializer.data)
    #districts = ["adilabad","karimnagar","warangal","khammam","nizamabad"]

