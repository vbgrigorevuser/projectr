from django.urls import path
from .views import start, register, login

app_name = 'managerauth'

urlpatterns = [
    path('start/', start, name='start'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
