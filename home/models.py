from django.db import models
from django_summernote.fields import SummernoteTextField


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = SummernoteTextField() 
