from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=100)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at   = models.DataTimeField(auto_now_add=True)
    updated_at   = models.DataTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

