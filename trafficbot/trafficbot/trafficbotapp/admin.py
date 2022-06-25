from django.contrib import admin
from .models import accidents, product

# Register your models here.
class productAdmin(admin.ModelAdmin):
    fileds=["offence_name","offence_section","fine"]
admin.site.register(product, productAdmin)
class accidentsadmin(admin.ModelAdmin):
    fields=["Do","Dont"]
admin.site.register(accidents,accidentsadmin)