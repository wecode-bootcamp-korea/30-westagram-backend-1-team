import json
import re 
import bcrypt

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        try:
            REGEX_EMAIL    = ('^[a-zA-Z0-9_-]+@[a-z]+\.[a-z]+')
            REGEX_PASSWORD = ('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
            
            data           = json.loads(request.body)
            name           = data['name']
            email          = data['email']
            password       = data['password']
            phone_number   = data['phone_number']
        
            if not re.match(REGEX_EMAIL,email):
                return JsonResponse({"message":"invalid_email"},status=400)
            
            if not re.match(REGEX_PASSWORD,password):
                return JsonResponse({"message":"invalid_password"},status=400)       
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message":"duplicate_email"}, status=400)
            
            if User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({"message":"duplicate_phone_number"}, status=400)
            
            new_salt        = bcrypt.gensalt()
            new_password    = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(new_password,new_salt) 
            decode_password = hashed_password.decode('utf-8')      
           
            User.objects.create(
                name         = name,
                email        = email,
                password     = decode_password,
                phone_number = phone_number,
            )
            return JsonResponse({"message":"success"},status=201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)
            
class LoginView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
           
            if not User.objects.filter(email = data['email'],password = data['password']).exists():
                return JsonResponse({"message":"INVALID_USER"},status=401)
            
            return JsonResponse({"message": "SUCCESS"}, status=200)  
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        