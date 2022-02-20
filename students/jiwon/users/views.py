import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user = User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                etc          = data['etc']
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

    def validate_email(email):
        REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if not re.fullmatch(REGEX_EMAIL, email):
            return JsonResponse(["이메일 형식을 확인하세요."])
        if User.objects.filter(email=email).exists():
            return JsonResponse({"message":"DUPLICATION_ERROR"}, status=400)

    def validate_password(password):
        REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
        if not re.fullmatch(REGEX_PASSWORD, password):
            return "비밀번호를 확인하세요. 최소 1개 이상의 소문자, 대문자, 숫자, 특수문자로 구성 되어야 하며 길이는 8자리 이상이어야 합니다."
            