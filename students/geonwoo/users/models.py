from django.db import models

# Create your models here.
class SignUp(models.Model):
    name        = models.CharField(max_length=10)
    email       = models.CharField(max_length=30)
    password    = models.IntegerField(null=True)
    phoneNumber = models.IntegerField(null=True)

    class Meta:
        db_table = "signUps"
    
