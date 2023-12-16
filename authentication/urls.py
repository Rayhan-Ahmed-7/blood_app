from django.urls import path

from .views import UserLoginAPIView, UserRegistrationAPIView

# from .views import LoginView


name = "authentication"
urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
]
