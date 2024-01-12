from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreation
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def Loginpage(request):
   
    if request.user.is_authenticated:
        return redirect('myapp:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Bunday username yuq!')

        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('myapp:home')
        else:
            messages.error(request, 'Username Yoki password Xato')

    context = {}
    return render(request, 'auth/login.html', context)

def Logoutpage(request):
    logout(request)
    return redirect('myapp:home')
def Register(request):
    form=UserCreation()
    if request.method=='POST':
        form=UserCreation(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect('myapp:home')
        else:
            messages.error(request,'Nimadir Xato Ketti!')
    context={'form':form}
    return render(request, 'auth/register.html', context)