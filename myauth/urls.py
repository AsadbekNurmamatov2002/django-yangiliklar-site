from django.urls import path
from .views import Loginpage, Register, Logoutpage

urlpatterns=[
    path('loginpage/',Loginpage,name='loginpage'),
    path('Register/',Register,name='register'),
    path('logoutpage/', Logoutpage, name='logoutpage'),
]