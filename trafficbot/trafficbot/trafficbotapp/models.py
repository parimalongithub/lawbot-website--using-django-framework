from django.db import models

# Create your models here.
class product(models.Model):
       offence_name=models.CharField(max_length=50)
       offence_section=models.CharField(max_length=300)
       fine=models.CharField(max_length=10)
class accidents(models.Model):
       Do=models.CharField(max_length=300)
       Dont=models.CharField(max_length=300)