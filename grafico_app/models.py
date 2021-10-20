from django.db import models

# Create your models here.
class Valores(models.Model):
    campo1=models.IntegerField()
    campo2=models.IntegerField()
    campo3=models.IntegerField()

class Tokens(models.Model):
    uuid=models.CharField(max_length=128)
    fecha=models.DateTimeField()
