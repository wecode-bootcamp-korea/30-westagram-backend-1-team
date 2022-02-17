from django.db import models

# Create your models here.
class UserInformation(models.Model):
    name        = models.CharField(max_length=20)
    email       = models.CharField(max_length=30)
    password    = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'
        