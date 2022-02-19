from django.shortcuts import render

import json, re

from django.http import JsonResponse
from django.views import View

from users.models import UserInformation

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']):
                return JsonResponse({'message':'Invalid_email'}, status=400)
            
            if not re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', data['password']):
                return JsonResponse({'message':'Invalid_password'}, status=400)  
            
            if UserInformation.objects.filter(email=data['email']).exists(): 
                    return JsonResponse({'message':'Overlapped_email'}, status=400)
            
            signup = UserInformation.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number']
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KeyError'}, status=400) 
            