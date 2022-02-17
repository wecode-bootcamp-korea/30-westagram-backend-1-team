from django.db import models

# Create your models here.
class Sign_up(models.Model):
    name        = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    password    = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)

    class Meta:
        db_table = "sign_ups"
    
