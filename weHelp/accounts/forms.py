from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'style:': 'text-align: right;', 'placeholder': 'מחמ'}),
            'password1': forms.TextInput(attrs={'class': 'input', 'style:': 'text-align: right;'}),
            'password2': forms.TextInput(attrs={'class': 'input', 'style:': 'text-align: right;'})
        }


class CreateAdult(forms.ModelForm):
    class Meta:
        model = models.adult
        fields = ['name', 'age', 'city', 'phone']


class CreateYoung(forms.ModelForm):
    class Meta:
        model = models.young
        fields = ['name', 'age', 'city', 'phone']
