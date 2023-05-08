from django.urls import path,include
from . import views
urlpatterns = [
    path("aqi-list/",views.AQI_PROPHETlist,name="aqiprophetlist-api"),
    path("warangaltemprature/",views.ALLTEMPLSTMwarangallist,name="tempofwarangal-lstm"),
    path("khammamtemprature/",views.ALLTEMPLSTMkhammamlist,name="tempofkhammam-lstm"),
    path("adilabadtemprature/",views.ALLTEMPLSTMadilabadlist,name="tempofadilabad-lstm"),
    path("nizamabadtemprature/",views.ALLTEMPLSTMnizamabadlist,name="tempofnizamabad-lstm"),
    path("karimnagartemprature/",views.ALLTEMPLSTMkarimnagarlist,name="tempofkarimnagar-lstm"),
    path("adilabadaqi/",views.AQIPhrophetadilabad,name="aqiofadilabad-phrophet"),
    path("nizamabadaqi/",views.AQIPhrophetnizamabad,name="aqiofnizamabad-phrophet"),
    path("khammamaqi/",views.AQIPhrophetkhammam,name="aqiofkhammam-phrophet"),
    path("karimnagaraqi/",views.AQIPhrophetkarimnagar,name="aqiofkarimnagar-phrophet"),
    path("warangalaqi/",views.AQIPhrophetwarangal,name="aqiofwarangal-phrophet"),
]