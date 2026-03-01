

from django.shortcuts import render

from django.shortcuts import redirect

from apps.users.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_view(request):
    if  request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Аккаунт создан успешно!')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request,'login.html',{
        'register_form':form,
        'login_form': AuthenticationForm(request),
        'show_register':True,
    })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request,'Invalid username or password')
    else:
        form = AuthenticationForm(request)
    return render(request,'login.html',{
    'login_form':form,
    'register_form':CustomUserCreationForm(),
    'show_register':False})


def logout_view(request):
    logout(request)
    return redirect('login')
