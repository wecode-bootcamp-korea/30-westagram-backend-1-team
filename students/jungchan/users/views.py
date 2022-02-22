import json
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from users.models     import User
from users.validation import valid_email, valid_password
from my_settings      import SECRET, ALGORITHM


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

            encoded_password = password.encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')
            
            signup = User.objects.create(
                name         = name,
                email        = email,
                password     = decoded_password,
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

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=400)

            user_password = User.objects.get(email=email).password

            if not bcrypt.checkpw(password.encode('utf-8'), user_password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=400)
            
            user         = User.objects.get(email=email)
            payload      = {'user-id':user.id}
            access_token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
        
            return JsonResponse({'token':access_token}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
