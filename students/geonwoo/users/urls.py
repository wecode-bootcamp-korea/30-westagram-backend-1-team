from django.urls import path
from users.views import UserView

urlpatterns = [
    path('/signups',UserView.as_view())
]