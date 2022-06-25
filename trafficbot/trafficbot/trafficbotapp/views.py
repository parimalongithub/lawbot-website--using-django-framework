
from django.shortcuts import render,HttpResponse

from trafficbotapp.admin import accidentsadmin
from .models import accidents
from .models import product

# Create your views here.
def home(request):
    #products=product.objects.all()
    return render(request,"home.html") 

def offence(request):
    products=product.objects.all()
    return render(request,"ofeence.html",{'products':products})

def accidentss(request):
    accident=accidents.objects.all()
    return render(request,"accidents.html",{"accident":accident})

                            


