from django.db import models
from django.db.models.deletion import SET_DEFAULT

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=35)
    detail=models.CharField(max_length=250)
    done=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)