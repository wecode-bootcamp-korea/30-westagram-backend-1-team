from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=50, unique=True)
    email        = models.CharField(max_length=50,unique=True)
    password     = models.CharField(max_length=150,unique=True)
    phone_number = models.CharField(max_length=50,unique=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
    
