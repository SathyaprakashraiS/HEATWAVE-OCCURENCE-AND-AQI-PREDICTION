from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("aqi/",views.aqi_chart,name="aqi"),
    path("tempadi/",views.tempadi,name="tempadi"),
    path("tempniz/",views.tempniz,name="tempniz"),
    path("tempkarim/",views.tempkarim,name="tempkarim"),
    path("tempkham/",views.tempkham,name="tempkham"),
    path("tempwar/",views.tempwar,name="tempwar"),
    path("adilabadaqi/",views.adilabadaqi,name="adilabad_aqi"),
    path("karimnagaraqi/",views.karimnagaraqi,name="adilabad_aqi"),
    path("khammamaqi/",views.khammamaqi,name="adilabad_aqi"),
    path("nizamabadaqi/",views.nizamabadaqi,name="adilabad_aqi"),
    path("warangalaqi/",views.warangalaqi,name="adilabad_aqi"),
    path("adilabadwave/",views.adilabadwavefinder,name="adlibad_heatwave"),
    path("khammamwave/",views.khammamwavefinder,name="adlibad_heatwave"),
    path("warangalwave/",views.warangalwavefinder,name="adlibad_heatwave"),
    path("karimnagarwave/",views.karimnagarwavefinder,name="adlibad_heatwave"),
    path("nizamabadwave/",views.nizamabadwavefinder,name="adlibad_heatwave"),
    path("aqi-list/",views.AQI_PROPHETlist,name="aqiprophetlist-api"),
]