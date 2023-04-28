from django.urls import path,include
from . import views
urlpatterns = [
    path("aqi-list/",views.AQI_PROPHETlist,name="aqiprophetlist-api"),
]