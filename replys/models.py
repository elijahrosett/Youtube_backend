from django.db import models

# Create your models here.

class SuperType(models.Model):
    user = models.ForeignKey(SuperType,on_delete=CASCADE)
    Comment = models.ForeignKey(SuperType,on_delete=CASCADE)
    text = models.CharField(max_length=255)