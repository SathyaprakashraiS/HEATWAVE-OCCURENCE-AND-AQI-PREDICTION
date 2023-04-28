from django.db import models

# Create your models here.

class AQI_PROPHET(models.Model):
    district = models.TextField(null=True)
    year = models.DateField(null=True)
    aqi = models.FloatField(null=True)

class AQI_ARIMA(models.Model):
    district = models.TextField(null=True)
    year = models.DateField(null=True)
    aqi = models.FloatField(null=True)

class TEMP_LSTM_ADILABADD(models.Model):
    district = models.TextField(null=True)
    mandal =models.TextField(null=True)
    date = models.DateField(null=True)
    temp = models.FloatField(null=True)

class TEMP_LSTM_KHAMMAM(models.Model):
    district = models.TextField(null=True)
    mandal =models.TextField(null=True)
    date = models.DateField(null=True)
    temp = models.FloatField(null=True)
    
class TEMP_LSTM_KARIMNAGAR(models.Model):
    district = models.TextField(null=True)
    mandal =models.TextField(null=True)
    date = models.DateField(null=True)
    temp = models.FloatField(null=True)

class TEMP_LSTM_NIZAMABAD(models.Model):
    district = models.TextField(null=True)
    mandal =models.TextField(null=True)
    date = models.DateField(null=True)
    temp = models.FloatField(null=True)

class TEMP_LSTM_WARANGAL(models.Model):
    district = models.TextField(null=True)
    mandal =models.TextField(null=True)
    date = models.DateField(null=True)
    temp = models.FloatField(null=True)