from django.db import models

# Create your models here.

TYPES = (
    ('aqi','AQI'),
    ('temprature', 'TEMPRATURE'),    
)


class Tips(models.Model):
	formodel=models.TextField(max_length=100,choices=TYPES,default="TEMPRATURE")
	tip=models.TextField(max_length=1000,default="the tip")
	minvaluesrange=models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
	maxvaluerange=models.DecimalField(max_digits=5,decimal_places=2,default=0.0)


