from django import forms
from mail.models import *


class SimpleForm(forms.Form):
    pass


class AddMailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['category', 'sender', 'recipients', 'subject', 'body']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sender': forms.TextInput(attrs={'placeholder': 'Отправитель', 'class': 'form-control'}),
            'recipients': forms.TextInput(attrs={'placeholder': 'Получатели', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'class': 'form-control'}),
        }
