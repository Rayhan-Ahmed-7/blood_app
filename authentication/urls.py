from django.urls import path

from .views import LoginView


name = 'authentication'
urlpatterns = [path("login/", LoginView.as_view(),name='login')]
