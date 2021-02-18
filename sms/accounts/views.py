from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def signin(request):
    if request.method == "POST":
        af = AuthenticationForm(data=request.POST)
        if af.is_valid():
            username = af.cleaned_data.get('username')
            raw_password = af.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                print("user is authenticated")
                login(request, user)
                return redirect(home)
            else:
                print("user is not authenticated")
    else:
        af = AuthenticationForm()
    return render(request, 'accounts/login.html', {'af': af})


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        rf = SignUpForm(request.POST)
        print(rf)
        if rf.is_valid():
            rf.save()
            return redirect(signin)
    else:
        rf = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': rf})


def signout(request):
    logout(request)
    return redirect(signin)


@login_required
def home(request):
    # print(request.user.is_student())
    return render(request, 'accounts/home.html')
    # return render(request, 'base.html')
