from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from .models import young


def signup_view(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user
            login(request, user)
            # undertand where to direct the user depend on useer's kind
            return redirect('accounts:check_page')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            # undertand where to direct the user depend on useer's kind
            return redirect('home')
            # return render(request, 'accounts/user.html')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')


@login_required(login_url="/ accounts/login/")
def adult_page(request):
    posts = request.user.adult.adult_post.all()
    context = {'posts': posts}
    return render(request, 'accounts/user.html', context)


@login_required(login_url="/ accounts/login/")
def check(request):
    return render(request, 'accounts/ask_for_kind.html')


def get_num_Cell(num):
    new_number = 0
    for i in range(len(num)):
        if num[i] >= "0" and num[i] <= "9":
            new_number = new_number*10+int(num[i])
    new = "+972" + str(new_number)
    return new


def adult_login(request):
    form = forms.CreateAdult(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            tele = request.POST.get('phone')
            instance.phone = get_num_Cell(tele)
            instance.Auser = request.user
            form.save()
            return redirect('home')
        else:
            form = forms.CreateAdult()
    return render(request, 'accounts/Alogin.html', {'form': form})


def young_login(request):
    form = forms.CreateYoung(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            tele = request.POST.get('phone')
            instance.phone = get_num_Cell(tele)
            instance.Yuser = request.user
            form.save()
            return redirect('home')
    else:
        form = forms.CreateYoung()
    return render(request, 'accounts/Ylogin.html', {'form': form})
