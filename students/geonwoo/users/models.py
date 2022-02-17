from django.db import models

# Create your models here.
class SignUp(models.Model):
    name        = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    password    = models.IntegerField(max_length=15)
    phoneNumber = models.IntegerField(max_length=15)

    class Meta:
        db_table = "signUps"
    
