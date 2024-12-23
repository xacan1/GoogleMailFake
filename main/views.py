from django.views.generic import FormView, RedirectView, CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from main.forms import *


# class PageNotFound(FormView, RedirectView):
#     form_class = SimpleForm
#     template_name = 'main/page404.html'
#     permanent = True
#     url = reverse_lazy('home')

#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
#         response.status_code = 404
#         return response


class PageNotFound(RedirectView):
    permanent = True
    url = reverse_lazy('home')


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('mail-list', kwargs={'category_slug': 'vhodyashie'})


class LogoutUserView(auth_views.LogoutView):
    next_page = 'login'


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    extra_context = {'title': 'Регистрация нового пользователя'}
    success_url = reverse_lazy('login')
