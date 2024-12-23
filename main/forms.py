from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class SimpleForm(forms.Form):
    pass


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Телефон или адрес эл. почты'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Password')}))


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password confirmation')}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password1', 'password2')
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя или название компании'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия', 'hidden': ''}), }
