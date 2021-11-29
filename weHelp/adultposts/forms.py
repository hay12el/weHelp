from django import forms
from django.db.models import fields
from django.forms import ModelForm
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea1', 'placeholder': 'כותרת', 'style:': 'text-align: right;'}),
            'text': forms.Textarea(attrs={'rows': '3', 'cols': '33', 'placeholder': 'טקסט חופשי', 'placeholder': 'טקסט חופשי', 'style:': 'text-align: right;'})
        }


class savePost(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['youngs']


class closed(forms.ModelForm):
    class Meta:
        model = models.post
        fields = []
