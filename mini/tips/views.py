from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect

import datetime

# Create your views here.
def hometips(request):
	return render(request,"hometips.html")

