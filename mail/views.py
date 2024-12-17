from django.views.generic import ListView, DetailView, CreateView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mail.forms import *
from mail.models import *


class RedirectIndexView(RedirectView):
    permanent = True
    url = 'mail/'


class MailListView(LoginRequiredMixin, ListView):
    form_class = SimpleForm
    template_name = 'mail/index.html'
    # paginate_by = 10
    login_url = reverse_lazy('login')
    context_object_name = 'emails'

    def get_queryset(self):
        user = self.request.user
        slug = self.kwargs.get('category_slug', '')

        if slug:
            queryset = Email.objects.select_related(
                'category').filter(user=user, category__slug=slug)
        else:
            queryset = Email.objects.filter(user=user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('category_slug', '')
        c_def = {'title': '', }

        if slug:
            queryset = Category.objects.filter(slug=slug)

            if queryset:
                category = queryset[0]
                c_def = {'title': f'{category.name} - {self.request.user}'}

        return {**context, **c_def}


class MailDetailView(LoginRequiredMixin, DetailView):
    model = Email
    template_name = 'mail/body_mail.html'
    pk_url_kwarg = 'email_pk'
    context_object_name = 'email'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Входящие'}
        return {**context, **c_def}

    def get_queryset(self):
        queryset = super().get_queryset()
        email = queryset[0]
        email.read = True
        email.save()
        return queryset


class MailCreateView(LoginRequiredMixin, CreateView):
    form_class = AddMailForm
    model = Email
    template_name = 'mail/add_mail.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('index')
