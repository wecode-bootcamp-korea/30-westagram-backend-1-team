import json
import re #유효성검사


from django.http  import JsonResponse
from django.views import View
from users.models import User
# Create your views here.
class UserView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            users = User.objects.all()
            email_condition = re.compile(
                    '^[a-zA-Z0-9_-]+@[a-z]+\.[a-z]+'
                )
            #이메일 정규표현식 앞에 []는 대문자소문자숫자모두가능하며^앞라인부터시작해야한다는것이고
            #두번째[]는 앞에꺼뒤에 @가와야하며 영문소문자가능하고 .도 마찬가지이고 대소문자가 가능하다는 의미이다.            
            password_condition =re.compile(
                   '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            ) 
            #최소 8자이상 1개이상의대소문자 1개이상의 특수문자 1개이상의숫자       
            validation_email    = email_condition.match(data['email'])
            validation_password = password_condition.match(data['password'])
            
            if validation_email    == None:
                return JsonResponse({"message":"invalid_email"},status=400)
            if validation_password == None:
                return JsonResponse({"message":"invalid_password"},status=400)       
            if users.filter(email = data["email"]).exists():
                return JsonResponse({"message":"duplicate_email"}, status=400)
            if users.filter(phone_number =data["phone_number"]):
                return JsonResponse({"message":"duplicate_phone_number"}, status=400)
            
            
            
            
            users = User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
            )
            return JsonResponse({"message":"success"},status=201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)
            
