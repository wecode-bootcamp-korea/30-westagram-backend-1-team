from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=50,unique=True)
    password     = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50,unique=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
    

#함수를 실행시켜서 회원가입이 되게끔 하는게 목적이죠.회원가입 유저의 정보를 데이터베이스에 저장하는게 목적이다..
