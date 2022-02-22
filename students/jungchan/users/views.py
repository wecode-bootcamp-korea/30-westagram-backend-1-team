import json, re

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validation import valid_email, valid_password

class SignupView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            if not valid_email(email):
                return JsonResponse({'message':'Invalid_email'}, status=400)
            
            if not valid_password(password):
                return JsonResponse({'message':'Invalid_password'}, status=400)  
            
            if User.objects.filter(email=email).exists(): 
                    return JsonResponse({'message':'Overlapped_email'}, status=400)
            
            signup = User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400) 
            
class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if User.objects.filter(email=email, password=password).exists():
                return JsonResponse({'message':'SUCCESS'}, status=200)
            
            else:
                return JsonResponse({'message':'INVALID_USER'}, status=400)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
