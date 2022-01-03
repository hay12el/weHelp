from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.models import young
from .models import post
from accounts.models import adult
from django.contrib.auth.decorators import login_required
from . import forms


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            instance.author = request.user.adult
            instance.phone = request.user.adult.phone
            instance.city = request.user.adult.city
            instance.selected_help = request.POST.get('select')

            form.save()
            return redirect('home')
    else:
        form = forms.CreatePost()
    return render(request, 'adultposts/post_create.html', {'form': form})


def current_post(request, pk):
    This_post = post.objects.get(id=pk)
    me = request.user.young.id
    hai = This_post.youngs.add(young.objects.get(id=me))

    if request.method == 'POST':
        posts1 = post.objects.all()
        return render(request, 'accounts/young_homepage.html', {'posts': posts1})

    return render(request, 'adultposts/current_post.html', {'post': This_post})
