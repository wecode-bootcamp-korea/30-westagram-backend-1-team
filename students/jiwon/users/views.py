import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            REGEX_EMAIL    = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
            
            if not re.match(REGEX_EMAIL, data["email"]):
                return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)

            if not re.match(REGEX_PASSWORD, data["password"]):
                return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)

            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse({"message":"VALIDATION_ERROR"}, status=400)

            user = User.objects.create(
                name         = data['name'], 
                email        = data['email'], 
                password     = data['password'],
                phone_number = data['phone_number']
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

class SigninView(View):
    def post(self, request):
        try :
            data = json.loads(request.body)

            if not User.objects.filter(email=data["email"], password=data["password"]):
                return JsonResponse({"message":"INVALID_USER"}, status=401)

            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        