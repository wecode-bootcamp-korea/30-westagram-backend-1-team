from django.urls import path, include
from users.views import UserView

urlpatterns = [
    path("users", include("users.urls"))
]
