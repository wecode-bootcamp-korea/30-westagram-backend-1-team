import json, re, bcrypt, jwt

from django.http  import JsonResponse, HttpResponse
from django.views import View

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            REGEX_EMAIL    = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
            
            if not re.match(REGEX_EMAIL, data["email"]):
                return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)

            if not re.match(REGEX_PASSWORD, data["password"]):
                return JsonResponse({"message":"VALIDATION_ERROR "}, status=400)
            
            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)

            encoded_pw = data["password"].encode('utf-8')
            hashed_pw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
            decoded_pw = hashed_pw.decode('utf-8')

            user = User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = decoded_pw,
                phone_number = data['phone_number'],
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

class SigninView(View):
    def post(self, request):
        try :
            data = json.loads(request.body)

            if not User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)

            user = User.objects.get(email=data["email"])
                
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message":"INVALID_PASSWORD"}, status=401)

            token = jwt.encode({"user_id":user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({"message":"SUCCESS", "token":token}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)



        
