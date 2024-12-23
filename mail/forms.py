from django import forms
from mail.models import *


class SimpleForm(forms.Form):
    pass


class AddMailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['user', 'category', 'sender',
                  'recipients', 'subject', 'body']
        widgets = {
            'user': forms.Select(attrs={'hidden': ''}),
            'category': forms.Select(attrs={'hidden': ''}),
            'sender': forms.TextInput(attrs={'placeholder': 'Отправитель', 'class': 'new__who-input'}),
            'recipients': forms.TextInput(attrs={'placeholder': 'Получатель', 'class': 'new__who-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема', 'class': 'new__input-title'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 14, 'class': 'new__input-textarea w-100'}),
        }
