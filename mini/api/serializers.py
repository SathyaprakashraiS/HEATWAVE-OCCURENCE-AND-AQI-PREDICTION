from rest_framework import serializers
from main.models import *

#from django.contrib.main.custom import User

class AQI_PROPHETSerializer(serializers.ModelSerializer):
	class Meta:
		model = AQI_PROPHET
		fields ='__all__'