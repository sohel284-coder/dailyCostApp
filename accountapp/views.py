from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

from accountapp.forms import CreateUserForm




def signup(request, ):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account has been Created for ' + user)
            return redirect('login')

    return render(request, 'authentication/register_page.html', {'form':form})


def login(request, ):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'authentication/login_page.html', )


def logout_user(request, ):
    logout(request)
    return redirect('login')
