from rest_framework import serializers
from main.models import *

#from django.contrib.main.custom import User

class AQI_PROPHETSerializer(serializers.ModelSerializer):
	class Meta:
		model = AQI_PROPHET
		fields ='__all__'

class ALLTEMP_khammam_LSTMSerializer(serializers.ModelSerializer):
	class Meta:
		model=TEMP_LSTM_KHAMMAM
		fields='__all__'

class ALLTEMP_warangal_LSTMSerializer(serializers.ModelSerializer):
	class Meta:
		model=TEMP_LSTM_WARANGAL
		fields='__all__'

class ALLTEMP_adilabad_LSTMSerializer(serializers.ModelSerializer):
	class Meta:
		model=TEMP_LSTM_ADILABADD
		fields='__all__'

class ALLTEMP_nizamabad_LSTMSerializer(serializers.ModelSerializer):
	class Meta:
		model=TEMP_LSTM_NIZAMABAD
		fields='__all__'

class ALLTEMP_karimnagar_LSTMSerializer(serializers.ModelSerializer):
	class Meta:
		model=TEMP_LSTM_KARIMNAGAR
		fields='__all__'


