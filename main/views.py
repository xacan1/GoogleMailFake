from django.views.generic import FormView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from main.forms import *


class PageNotFound(FormView):
    form_class = SimpleForm
    template_name = 'main/page404.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.status_code = 404
        return response


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('mail-list', kwargs={'category_slug': 'vhodyashie'})


class LogoutUserView(auth_views.LogoutView):
    next_page = 'login'
