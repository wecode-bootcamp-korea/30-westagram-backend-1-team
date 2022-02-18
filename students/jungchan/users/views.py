from django.shortcuts import render

# Create your views here.
import json, re

from django.http import JsonResponse
from django.views import View

from users.models import UserInformation

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not data['email'] or not data['password']:
                return JsonResponse({'message':'KEY_ERROR'}, status=400)
            # email과 password가 입력되지 않았을 경우 띄워주는 경고
            if re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']) == None:
                return JsonResponse({'message':'Invalid_email'}, status=400)
            # email이 형식에 맞지 않았을 경우에 띄워주는 경고
            if re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', data['password']) == None:
                return JsonResponse({'message':'Invalid_password'}, status=400)  
            # password가 형식에 맞지 않았을 경우에 띄워주는 경고
            userinformations = UserInformation.objects.all()  # db에 저장된 모든 정보를 불러와서 변수에 저장
            for user_email in userinformations:
                if user_email.email == data['email']: 
                    return JsonResponse({'message':'Overlapped_email'}, status=400)
            # for문 돌려서 저장되어져있는 email 값과 회원가입시 입력된 email값이 중복되지 않는지 확인
            
            signup = UserInformation.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number']
            )
            # 전부 형식에 맞게 입력했을 경우 회원정보 db에 create 
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400) 
