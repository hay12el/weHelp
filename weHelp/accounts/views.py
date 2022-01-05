from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from .models import adult, young
from adultposts.models import post


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
            if request.user.is_superuser:
                return admin_homepage(request)
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
            instance.Yuser = request.user
            form.save()
            return redirect('home')
    else:
        form = forms.CreateYoung()
    return render(request, 'accounts/Ylogin.html', {'form': form})


@login_required(login_url="/ accounts/login/")
def young_hompage(request):
    posts1 = post.objects.all()

    if request.method == 'GET':
        val = request.GET.get("city")
        if not val:
            return render(request, 'accounts/young_homepage.html', {'posts': posts1})
        posts1 = post.objects.filter(city__contains=val)
        return render(request, 'accounts/young_homepage.html', {'posts': posts1})

    return render(request, 'accounts/young_homepage.html', {'posts': posts1})


@login_required(login_url="/ accounts/login/")
def young_saved_posts(request):
    current_user = request.user
    me = young.objects.get(id=current_user.young.id)
    myPosts = post.objects.filter(youngs=me)
    return render(request, 'accounts/saved_posts.html', {'posts': myPosts})


@login_required(login_url="/ accounts/login/")
def got_helped(request, pk):
    The_post = post.objects.get(id=pk)
    if The_post.status == False:
        The_post.status = True
    else:
        The_post.status = False
    The_post.save()
    current_user = request.user
    me = young.objects.get(id=current_user.young.id)
    myPosts = post.objects.filter(youngs=me)
    return render(request, 'accounts/saved_posts.html', {'posts': myPosts})


@login_required(login_url="/ accounts/login/")
def admin_homepage(request):
    posts = post.objects.all()
    adults = adult.objects.all()
    youngs = young.objects.all()
    num_of_posts = posts.count()
    num_of_youngs = youngs.count()
    num_of_adults = adults.count()
    got_help = post.objects.filter(status=True)
    yet = num_of_posts - got_help.count()
    print(num_of_posts, num_of_adults, num_of_youngs, yet)
    context = {'posts': num_of_posts,
               'youngs': num_of_youngs,
               'adults': num_of_adults,
               'got_help': got_help.count(),
               'yet': yet}
    return render(request, 'accounts/admin_homepage.html', context)


@login_required(login_url="/ accounts/login/")
def admin_adult(request):
    adults = adult.objects.all()
    return render(request, 'accounts/admin_adults.html', {'adults': adults})


@login_required(login_url="/ accounts/login/")
def admin_young(request):
    youngs = young.objects.all()
    return render(request, 'accounts/admin_youngs.html', {'youngs': youngs})


@login_required(login_url="/ accounts/login/")
def admin_posts(request):
    posts = post.objects.all()
    return render(request, 'accounts/admin_posts.html', {'posts': posts})


@login_required(login_url="/ accounts/login/")
def delete_young(request, pk):
    obj = young.objects.get(id=pk)
    obj.delete()
    youngs = young.objects.all()
    return render(request, 'accounts/admin_youngs.html', {'youngs': youngs})


@login_required(login_url="/ accounts/login/")
def delete_adult(request, pk):
    obj = adult.objects.get(id=pk)
    obj.delete()
    adults = adult.objects.all()
    return render(request, 'accounts/admin_adults.html', {'adults': adults})


@login_required(login_url="/ accounts/login/")
def delete_post(request, pk):
    obj = post.objects.get(id=pk)
    obj.delete()
    posts = post.objects.all()
    return render(request, 'accounts/admin_posts.html', {'posts': posts})


@login_required(login_url="/ accounts/login/")
def admin_got_helped(request, pk):
    The_post = post.objects.get(id=pk)
    if The_post.status == False:
        The_post.status = True
    else:
        The_post.status = False
    The_post.save()
    posts = post.objects.all()
    return render(request, 'accounts/admin_posts.html', {'posts': posts})