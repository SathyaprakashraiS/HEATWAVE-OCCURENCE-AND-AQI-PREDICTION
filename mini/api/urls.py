from django.urls import path,include
from . import views
urlpatterns = [
    path("aqi-list/",views.AQI_PROPHETlist,name="aqiprophetlist-api"),
    path("warangaltemprature/",views.ALLTEMPLSTMwarangallist,name="tempofwarangal-lstm"),
    path("khammamtemprature/",views.ALLTEMPLSTMkhammamlist,name="tempofkhammam-lstm"),
    path("adilabadtemprature/",views.ALLTEMPLSTMadilabadlist,name="tempofadilabad-lstm"),
    path("nizamabadtemprature/",views.ALLTEMPLSTMnizamabadlist,name="tempofnizamabad-lstm"),
    path("karimnagartemprature/",views.ALLTEMPLSTMkarimnagarlist,name="tempofkarimnagar-lstm"),
]