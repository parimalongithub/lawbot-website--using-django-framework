from django.contrib import admin
from django.urls import path
from trafficbotapp import views

urlpatterns = [

    path("",views.home,name='home'),
    path("offence",views.offence,name='offence'),
    path("accidents",views.accidentss,name="accidents")
]

