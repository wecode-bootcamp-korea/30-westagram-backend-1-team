from django.urls import path, include
from users.views import SignupView

urlpatterns = [
    path("users", include("users.urls"))
]
