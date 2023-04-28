from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view

from django.http import JsonResponse
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from api.serializers import *

import datetime

# Create your views here.
def home(request):
    # empty_record = AQI_ARIMA.objects.filter(district__isnull=True)
    # empty_record.delete()
    return render(request,"home.html")



import plotly.graph_objs as go

def aqi_chart(request):
    districts = ["adilabad","karimnagar","warangal","khammam","nizamabad"]
    readings = AQI_PROPHET.objects.filter(district__in=districts)

    color_map = {'adilabad': 'blue', 'karimnagar': 'red', 'warangal': 'green','khammam':'yellow','nizamabad':'orange'}

    data = []
    for district in districts:
        district_readings = readings.filter(district=district)
        dates = [reading.year for reading in district_readings]
        aqi_levels = [reading.aqi for reading in district_readings]
        data.append(go.Scatter(x=dates, y=aqi_levels, name=district, line=dict(color=color_map[district])))

    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'aqi.html', {'chart_div': chart_div})



def tempadi(request):
    readings = TEMP_LSTM_ADILABADD.objects.all()

    # Create lists for the x and y values of the chart
    dates = [reading.date for reading in readings]
    temperature = [reading.temp for reading in readings]

    # Create the Plotly chart
    data = [go.Scatter(x=dates, y=temperature)]
    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Temperature in Celsius'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'tempadi.html', {'chart_div': chart_div})


def tempniz(request):
    readings = TEMP_LSTM_NIZAMABAD.objects.all()

    # Create lists for the x and y values of the chart
    dates = [reading.date for reading in readings]
    temperature = [reading.temp for reading in readings]

    # Create the Plotly chart
    data = [go.Scatter(x=dates, y=temperature)]
    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Temperature in Celsius'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'tempniz.html', {'chart_div': chart_div})

def tempkarim(request):
    readings = TEMP_LSTM_KARIMNAGAR.objects.all()

    # Create lists for the x and y values of the chart
    dates = [reading.date for reading in readings]
    temperature = [reading.temp for reading in readings]

    # Create the Plotly chart
    data = [go.Scatter(x=dates, y=temperature,line=dict(color="green"))]
    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Temperature in Celsius'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'tempkarim.html', {'chart_div': chart_div})

def tempkham(request):
    readings = TEMP_LSTM_KHAMMAM.objects.all()

    # Create lists for the x and y values of the chart
    dates = [reading.date for reading in readings]
    temperature = [reading.temp for reading in readings]

    # Create the Plotly chart
    data = [go.Scatter(x=dates, y=temperature)]
    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Temperature in Celsius'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'tempkham.html', {'chart_div': chart_div})


def tempwar(request):
    readings = TEMP_LSTM_WARANGAL.objects.all()

    # Create lists for the x and y values of the chart
    dates = [reading.date for reading in readings]
    temperature = [reading.temp for reading in readings]

    # Create the Plotly chart
    data = [go.Scatter(x=dates, y=temperature)]
    layout = go.Layout(title='AQI Levels Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Temperature in Celsius'))
    chart = go.Figure(data=data, layout=layout)
    chart_div = chart.to_html(full_html=False)

    return render(request, 'tempwar.html', {'chart_div': chart_div})

def adilabadaqi(request):
    adilabadaqi=AQI_PROPHET.objects.all().filter(district="adilabad")
    values="asd"

    data=[]
    dates=[]
    dataa=[]
    color="green"
    for i in adilabadaqi:
        dates.append(i.year)
        data.append(i.aqi)

    lastaqis=AQI_PROPHET.objects.filter(district="adilabad").order_by('-id')[:24]
    lastaqis_in_ascending_order=reversed(lastaqis)


    dataa.append(go.Scatter(x=dates, y=data, name="adilbad", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)

    data2024=[]
    dates2024=[]
    dataa2024=[]
    color2024="blue"
    for i in lastaqis_in_ascending_order:
        dates2024.append(i.year)
        data2024.append(i.aqi)

    dataa2024.append(go.Scatter(x=dates2024, y=data2024, name="adilbad", line=dict(color=color2024)))
    layout2024 = go.Layout(title='', xaxis=dict(title='month'), yaxis=dict(title='AQI Level'))
    chart2024 = go.Figure(data=dataa2024, layout=layout2024)
    chart_div_2024 = chart2024.to_html(full_html=False)

    #print("length of adilabad aqi is",len(adilabadaqi))
    return render(request,'adilabadaqi.html',{"adilabadaqi":adilabadaqi,"chart_div":chart_div,"predictedyear":lastaqis_in_ascending_order,"chart_div_2024":chart_div_2024})

def warangalaqi(request):
    adilabadaqi=AQI_PROPHET.objects.all().filter(district="warangal")
    values="asd"

    data=[]
    dates=[]
    dataa=[]
    color="green"
    for i in adilabadaqi:
        dates.append(i.year)
        data.append(i.aqi)

    lastaqis=AQI_PROPHET.objects.filter(district="warangal").order_by('-id')[:24]
    lastaqis_in_ascending_order=reversed(lastaqis)


    dataa.append(go.Scatter(x=dates, y=data, name="warangal", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)

    data2024=[]
    dates2024=[]
    dataa2024=[]
    color2024="blue"
    for i in lastaqis_in_ascending_order:
        dates2024.append(i.year)
        data2024.append(i.aqi)

    dataa2024.append(go.Scatter(x=dates2024, y=data2024, name="warangal", line=dict(color=color2024)))
    layout2024 = go.Layout(title='', xaxis=dict(title='month'), yaxis=dict(title='AQI Level'))
    chart2024 = go.Figure(data=dataa2024, layout=layout2024)
    chart_div_2024 = chart2024.to_html(full_html=False)

    #print("length of warangal aqi is",len(adilabadaqi))
    return render(request,'warangalaqi.html',{"adilabadaqi":adilabadaqi,"chart_div":chart_div,"predictedyear":lastaqis_in_ascending_order,"chart_div_2024":chart_div_2024})

def karimnagaraqi(request):
    adilabadaqi=AQI_PROPHET.objects.all().filter(district="karimnagar")
    values="asd"

    data=[]
    dates=[]
    dataa=[]
    color="green"
    for i in adilabadaqi:
        dates.append(i.year)
        data.append(i.aqi)

    lastaqis=AQI_PROPHET.objects.filter(district="karimnagar").order_by('-id')[:24]
    lastaqis_in_ascending_order=reversed(lastaqis)


    dataa.append(go.Scatter(x=dates, y=data, name="karimnagar", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)

    data2024=[]
    dates2024=[]
    dataa2024=[]
    color2024="blue"
    for i in lastaqis_in_ascending_order:
        dates2024.append(i.year)
        data2024.append(i.aqi)

    dataa2024.append(go.Scatter(x=dates2024, y=data2024, name="karimnagar", line=dict(color=color2024)))
    layout2024 = go.Layout(title='', xaxis=dict(title='month'), yaxis=dict(title='AQI Level'))
    chart2024 = go.Figure(data=dataa2024, layout=layout2024)
    chart_div_2024 = chart2024.to_html(full_html=False)

    #print("length of karimnagar aqi is",len(adilabadaqi))
    return render(request,'karimnagaraqi.html',{"adilabadaqi":adilabadaqi,"chart_div":chart_div,"predictedyear":lastaqis_in_ascending_order,"chart_div_2024":chart_div_2024})

def khammamaqi(request):
    adilabadaqi=AQI_PROPHET.objects.all().filter(district="khammam")
    values="asd"

    data=[]
    dates=[]
    dataa=[]
    color="green"
    for i in adilabadaqi:
        dates.append(i.year)
        data.append(i.aqi)

    lastaqis=AQI_PROPHET.objects.filter(district="khammam").order_by('-id')[:24]
    lastaqis_in_ascending_order=reversed(lastaqis)


    dataa.append(go.Scatter(x=dates, y=data, name="khammam", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)

    data2024=[]
    dates2024=[]
    dataa2024=[]
    color2024="blue"
    for i in lastaqis_in_ascending_order:
        dates2024.append(i.year)
        data2024.append(i.aqi)

    dataa2024.append(go.Scatter(x=dates2024, y=data2024, name="khammam", line=dict(color=color2024)))
    layout2024 = go.Layout(title='', xaxis=dict(title='month'), yaxis=dict(title='AQI Level'))
    chart2024 = go.Figure(data=dataa2024, layout=layout2024)
    chart_div_2024 = chart2024.to_html(full_html=False)

    #print("length of khammam aqi is",len(adilabadaqi))
    return render(request,'khammamaqi.html',{"adilabadaqi":adilabadaqi,"chart_div":chart_div,"predictedyear":lastaqis_in_ascending_order,"chart_div_2024":chart_div_2024})

def nizamabadaqi(request):
    adilabadaqi=AQI_PROPHET.objects.all().filter(district="nizamabad")
    values="asd"

    data=[]
    dates=[]
    dataa=[]
    color="green"
    for i in adilabadaqi:
        dates.append(i.year)
        data.append(i.aqi)

    lastaqis=AQI_PROPHET.objects.filter(district="nizamabad").order_by('-id')[:24]
    lastaqis_in_ascending_order=reversed(lastaqis)


    dataa.append(go.Scatter(x=dates, y=data, name="nizamabad", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title='AQI Level'))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)

    data2024=[]
    dates2024=[]
    dataa2024=[]
    color2024="blue"
    for i in lastaqis_in_ascending_order:
        dates2024.append(i.year)
        data2024.append(i.aqi)

    dataa2024.append(go.Scatter(x=dates2024, y=data2024, name="nizamabad", line=dict(color=color2024)))
    layout2024 = go.Layout(title='', xaxis=dict(title='month'), yaxis=dict(title='AQI Level'))
    chart2024 = go.Figure(data=dataa2024, layout=layout2024)
    chart_div_2024 = chart2024.to_html(full_html=False)

    #print("length of nizamabad aqi is",len(adilabadaqi))
    return render(request,'nizamabadaqi.html',{"adilabadaqi":adilabadaqi,"chart_div":chart_div,"predictedyear":lastaqis_in_ascending_order,"chart_div_2024":chart_div_2024})
































def adilabadwavefinder(request):
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    
    #date_string="2022-10-30"

    currentdataval=TEMP_LSTM_ADILABADD.objects.all().filter(district="Adilabad",date=date_string)
    ##print("current data temp is",currentdataval)

    lastdata=TEMP_LSTM_ADILABADD.objects.all().filter(district="Adilabad").order_by('-id')[:35]
    lastdata_in_ascending_order=reversed(lastdata)
    data=[]
    dates=[]
    dataa=[]

    assumedavg=0
    for i in lastdata_in_ascending_order:
        ##print(i.date)
        ##print(i.temp)
        dates.append(i.date)
        data.append(i.temp)
        assumedavg+=i.temp

    color="green"

    # #print("dates length ",len(dates))
    # #print("data length ",len(data))

    assumedavg=assumedavg/35
    heatwave=[]

    def checker(i,dates,data,assumedavg):
        val=0
        tval=0
        tempo=i
        if(i<len(dates)-1):
            if(data[i+1]>=assumedavg):
                val+=1
                tval,tempo=checker(i+1,dates,data,assumedavg)
                val+=tval
                return val,tempo
        return val,tempo

    wavelength=0
    wavestart=[]
    waveend=[]
    waveslen=[]
    i=0
    while(i<len(dates)):
        wavelength=0
        if(data[i]>=assumedavg):
            #wavestart.append(dates[i])
            wavelength,tempi=checker(i,dates,data,assumedavg)
            wavelength+=1
            #waveend.append(dates[i])
            #waveslen.append(wavelength)
            if(i==tempi):
                i+=1
            else:
                wavestart.append(dates[i])
                waveend.append(dates[tempi])
                waveslen.append(wavelength)
                i=tempi
            #print("tempi is ",tempi,i)
            #i+=1
        else:
            i+=1

    #print("total heat waves:",len(wavestart))
    # for i in range(len(wavestart)):
    #     #print("heatwave starts at ",wavestart[i])
    #     #print("heat wave ends at ",waveend[i])
    #     #print("wavelength ",waveslen[i])
    # #print(" assumed average avg temprature is ",assumedavg)

    dataa.append(go.Scatter(x=dates, y=data, name="adilbad", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title="Temprature"))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)
    numofwaves=len(wavestart)
    return render(request,"adilabadwave.html",{"chart_div":chart_div,"wavestart":wavestart,"waveend":waveend,"waveslen":waveslen,"assumedavg":assumedavg,"currentdataval":currentdataval,"numofwaves":numofwaves})

def khammamwavefinder(request):
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    
    #date_string="2022-10-30"

    currentdataval=TEMP_LSTM_KHAMMAM.objects.all().filter(district="Khammam",date=date_string)
    # #print("current data temp is",currentdataval)

    lastdata=TEMP_LSTM_KHAMMAM.objects.all().filter(district="Khammam").order_by('-id')[:35]
    lastdata_in_ascending_order=reversed(lastdata)
    data=[]
    dates=[]
    dataa=[]

    assumedavg=0
    for i in lastdata_in_ascending_order:
        #print(i.date)
        #print(i.temp)
        dates.append(i.date)
        data.append(i.temp)
        assumedavg+=i.temp

    color="green"

    # #print("dates length ",len(dates))
    # #print("data length ",len(data))

    assumedavg=assumedavg/35
    heatwave=[]

    def checker(i,dates,data,assumedavg):
        val=0
        tval=0
        tempo=i
        if(i<len(dates)-1):
            if(data[i+1]>=assumedavg):
                val+=1
                tval,tempo=checker(i+1,dates,data,assumedavg)
                val+=tval
                return val,tempo
        return val,tempo

    wavelength=0
    wavestart=[]
    waveend=[]
    waveslen=[]
    i=0
    while(i<len(dates)):
        wavelength=0
        if(data[i]>=assumedavg):
            #wavestart.append(dates[i])
            wavelength,tempi=checker(i,dates,data,assumedavg)
            wavelength+=1
            #waveend.append(dates[i])
            #waveslen.append(wavelength)
            if(i==tempi):
                i+=1
            else:
                wavestart.append(dates[i])
                waveend.append(dates[tempi])
                waveslen.append(wavelength)
                i=tempi
            #print("tempi is ",tempi,i)
            #i+=1
        else:
            i+=1

    #print("total heat waves:",len(wavestart))
    # for i in range(len(wavestart)):
    #     #print("heatwave starts at ",wavestart[i])
    #     #print("heat wave ends at ",waveend[i])
    #     #print("wavelength ",waveslen[i])
    # #print(" assumed average avg temprature is ",assumedavg)

    dataa.append(go.Scatter(x=dates, y=data, name="khammam", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title="Temprature"))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)
    numofwaves=len(wavestart)
    return render(request,"khammamwave.html",{"chart_div":chart_div,"wavestart":wavestart,"waveend":waveend,"waveslen":waveslen,"assumedavg":assumedavg,"currentdataval":currentdataval,"numofwaves":numofwaves})

def warangalwavefinder(request):
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    
    #date_string="2022-10-30"

    currentdataval=TEMP_LSTM_WARANGAL.objects.all().filter(district="Warangal Urban",date=date_string)
    #print("current data temp is",currentdataval)

    lastdata=TEMP_LSTM_WARANGAL.objects.all().filter(district="Warangal Urban").order_by('-id')[:35]
    lastdata_in_ascending_order=reversed(lastdata)
    data=[]
    dates=[]
    dataa=[]

    assumedavg=0
    for i in lastdata_in_ascending_order:
        #print(i.date)
        #print(i.temp)
        dates.append(i.date)
        data.append(i.temp)
        assumedavg+=i.temp

    color="green"

    #print("dates length ",len(dates))
    #print("data length ",len(data))

    assumedavg=assumedavg/35
    heatwave=[]

    def checker(i,dates,data,assumedavg):
        val=0
        tval=0
        tempo=i
        if(i<len(dates)-1):
            if(data[i+1]>=assumedavg):
                val+=1
                tval,tempo=checker(i+1,dates,data,assumedavg)
                val+=tval
                return val,tempo
        return val,tempo

    wavelength=0
    wavestart=[]
    waveend=[]
    waveslen=[]
    i=0
    while(i<len(dates)):
        wavelength=0
        if(data[i]>=assumedavg):
            #wavestart.append(dates[i])
            wavelength,tempi=checker(i,dates,data,assumedavg)
            wavelength+=1
            #waveend.append(dates[i])
            #waveslen.append(wavelength)
            if(i==tempi):
                i+=1
            else:
                wavestart.append(dates[i])
                waveend.append(dates[tempi])
                waveslen.append(wavelength)
                i=tempi
            #print("tempi is ",tempi,i)
            #i+=1
        else:
            i+=1

    #print("total heat waves:",len(wavestart))
    #for i in range(len(wavestart)):
        #print("heatwave starts at ",wavestart[i])
        #print("heat wave ends at ",waveend[i])
        #print("wavelength ",waveslen[i])
    #print(" assumed average avg temprature is ",assumedavg)

    dataa.append(go.Scatter(x=dates, y=data, name="warangal", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title="Temprature"))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)
    numofwaves=len(wavestart)
    return render(request,"warangalwave.html",{"chart_div":chart_div,"wavestart":wavestart,"waveend":waveend,"waveslen":waveslen,"assumedavg":assumedavg,"currentdataval":currentdataval,"numofwaves":numofwaves})

def karimnagarwavefinder(request):
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    
    #date_string="2022-10-30"

    currentdataval=TEMP_LSTM_KARIMNAGAR.objects.all().filter(district="Karimnagar",date=date_string)
    #print("current data temp is",currentdataval)

    lastdata=TEMP_LSTM_KARIMNAGAR.objects.all().filter(district="Karimnagar").order_by('-id')[:35]
    lastdata_in_ascending_order=reversed(lastdata)
    data=[]
    dates=[]
    dataa=[]

    assumedavg=0
    for i in lastdata_in_ascending_order:
        #print(i.date)
        #print(i.temp)
        dates.append(i.date)
        data.append(i.temp)
        assumedavg+=i.temp

    color="green"

    #print("dates length ",len(dates))
    #print("data length ",len(data))

    assumedavg=assumedavg/35
    heatwave=[]

    def checker(i,dates,data,assumedavg):
        val=0
        tval=0
        tempo=i
        if(i<len(dates)-1):
            if(data[i+1]>=assumedavg):
                val+=1
                tval,tempo=checker(i+1,dates,data,assumedavg)
                val+=tval
                return val,tempo
        return val,tempo

    wavelength=0
    wavestart=[]
    waveend=[]
    waveslen=[]
    i=0
    while(i<len(dates)):
        wavelength=0
        if(data[i]>=assumedavg):
            #wavestart.append(dates[i])
            wavelength,tempi=checker(i,dates,data,assumedavg)
            wavelength+=1
            #waveend.append(dates[i])
            #waveslen.append(wavelength)
            if(i==tempi):
                i+=1
            else:
                wavestart.append(dates[i])
                waveend.append(dates[tempi])
                waveslen.append(wavelength)
                i=tempi
            #print("tempi is ",tempi,i)
            #i+=1
        else:
            i+=1

    #print("total heat waves:",len(wavestart))
    #for i in range(len(wavestart)):
        #print("heatwave starts at ",wavestart[i])
        #print("heat wave ends at ",waveend[i])
        #print("wavelength ",waveslen[i])
    #print(" assumed average avg temprature is ",assumedavg)

    dataa.append(go.Scatter(x=dates, y=data, name="Karimnagar", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title="Temprature"))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)
    numofwaves=len(wavestart)
    return render(request,"karimnagarwave.html",{"chart_div":chart_div,"wavestart":wavestart,"waveend":waveend,"waveslen":waveslen,"assumedavg":assumedavg,"currentdataval":currentdataval,"numofwaves":numofwaves})

def nizamabadwavefinder(request):
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    
    #date_string="2022-10-30"

    currentdataval=TEMP_LSTM_NIZAMABAD.objects.all().filter(district="Nizamabad",date=date_string)
    #print("current data temp is",currentdataval)

    lastdata=TEMP_LSTM_NIZAMABAD.objects.all().filter(district="Nizamabad").order_by('-id')[:35]
    lastdata_in_ascending_order=reversed(lastdata)
    data=[]
    dates=[]
    dataa=[]

    assumedavg=0
    for i in lastdata_in_ascending_order:
        #print(i.date)
        #print(i.temp)
        dates.append(i.date)
        data.append(i.temp)
        assumedavg+=i.temp

    color="green"

    #print("dates length ",len(dates))
    #print("data length ",len(data))

    assumedavg=assumedavg/35
    heatwave=[]

    def checker(i,dates,data,assumedavg):
        val=0
        tval=0
        tempo=i
        if(i<len(dates)-1):
            if(data[i+1]>=assumedavg):
                val+=1
                tval,tempo=checker(i+1,dates,data,assumedavg)
                val+=tval
                return val,tempo
        return val,tempo

    wavelength=0
    wavestart=[]
    waveend=[]
    waveslen=[]
    i=0
    while(i<len(dates)):
        wavelength=0
        if(data[i]>=assumedavg):
            #wavestart.append(dates[i])
            wavelength,tempi=checker(i,dates,data,assumedavg)
            wavelength+=1
            #waveend.append(dates[i])
            #waveslen.append(wavelength)
            if(i==tempi):
                i+=1
            else:
                wavestart.append(dates[i])
                waveend.append(dates[tempi])
                waveslen.append(wavelength)
                i=tempi
            #print("tempi is ",tempi,i)
            #i+=1
        else:
            i+=1

    #print("total heat waves:",len(wavestart))
    #for i in range(len(wavestart)):
        #print("heatwave starts at ",wavestart[i])
        #print("heat wave ends at ",waveend[i])
        #print("wavelength ",waveslen[i])
    #print(" assumed average avg temprature is ",assumedavg)

    dataa.append(go.Scatter(x=dates, y=data, name="Nizamabad", line=dict(color=color)))
    layout = go.Layout(title='', xaxis=dict(title='year'), yaxis=dict(title="Temprature"))
    chart = go.Figure(data=dataa, layout=layout)
    chart_div = chart.to_html(full_html=False)
    numofwaves=len(wavestart)
    return render(request,"nizamabadwave.html",{"chart_div":chart_div,"wavestart":wavestart,"waveend":waveend,"waveslen":waveslen,"assumedavg":assumedavg,"currentdataval":currentdataval,"numofwaves":numofwaves})


#API
@api_view(['GET'])
def AQI_PROPHETlist(request):
    books = AQI_PROPHET.objects.all().order_by('-id')
    serializer = AQI_PROPHETSerializer(books, many=True)
    return Response(serializer.data)