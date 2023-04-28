from django.contrib import admin
from .models import AQI_PROPHET
from .models import AQI_ARIMA
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources

class AQIResource(resources.ModelResource):

    class Meta:
        model = AQI_PROPHET

class AQIAdmin(ImportExportModelAdmin):
    resource_class = AQIResource

class AQIARIMA(resources.ModelResource):


    class Meta:
        model = AQI_ARIMA

class AQIARIMAAdmin(ImportExportModelAdmin):
    resource_class = AQIARIMA

class TEMP_LSTM_ADL(resources.ModelResource):

    class Meta:
        model = TEMP_LSTM_ADILABADD

class TEMP_LSTM_ADL_Admin(ImportExportModelAdmin):
    resource_class = TEMP_LSTM_ADL


class TEMP_LSTM_KHA(resources.ModelResource):

    class Meta:
        model = TEMP_LSTM_KHAMMAM

class TEMP_LSTM_KHA_Admin(ImportExportModelAdmin):
    resource_class = TEMP_LSTM_KHA

class TEMP_LSTM_KHARIM(resources.ModelResource):

    class Meta:
        model = TEMP_LSTM_KARIMNAGAR

class TEMP_LSTM_KHARIM_Admin(ImportExportModelAdmin):
    resource_class = TEMP_LSTM_KHARIM


class TEMP_LSTM_NIZ(resources.ModelResource):

    class Meta:
        model = TEMP_LSTM_NIZAMABAD

class TEMP_LSTM_NIZ_Admin(ImportExportModelAdmin):
    resource_class = TEMP_LSTM_NIZ


class TEMP_LSTM_WAR(resources.ModelResource):

    class Meta:
        model = TEMP_LSTM_WARANGAL

class TEMP_LSTM_WAR_Admin(ImportExportModelAdmin):
    resource_class = TEMP_LSTM_WAR


admin.site.register(AQI_PROPHET,AQIAdmin)
admin.site.register(AQI_ARIMA,AQIARIMAAdmin)
admin.site.register(TEMP_LSTM_ADILABADD,TEMP_LSTM_ADL_Admin)
admin.site.register(TEMP_LSTM_KHAMMAM,TEMP_LSTM_KHA_Admin)
admin.site.register(TEMP_LSTM_KARIMNAGAR,TEMP_LSTM_KHARIM_Admin)
admin.site.register(TEMP_LSTM_NIZAMABAD,TEMP_LSTM_NIZ_Admin)
admin.site.register(TEMP_LSTM_WARANGAL,TEMP_LSTM_WAR_Admin)
