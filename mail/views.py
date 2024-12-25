from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from mail.forms import *
from mail.models import *


class RedirectIndexView(RedirectView):
    permanent = True
    url = reverse_lazy('home')


class MailListView(LoginRequiredMixin, FormView):
    form_class = AddMailForm
    template_name = 'mail/index.html'
    # paginate_by = 10
    login_url = reverse_lazy('login')
    # context_object_name = 'emails'
    success_url = reverse_lazy('home')

    def get_emails(self):
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

        c_def['emails'] = self.get_emails()

        return {**context, **c_def}

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['category'] = Category.objects.filter(slug='otpravlennye')[0]
        initial['sender'] = self.request.user.email
        return initial

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            Email.objects.create(**form.cleaned_data)

        return response


class MailDetailView(LoginRequiredMixin, DetailView, CreateView):
    form_class = AddMailForm
    model = Email
    template_name = 'mail/body_mail.html'
    pk_url_kwarg = 'email_pk'
    context_object_name = 'email'
    login_url = reverse_lazy('login')

    # ответить на письмо
    def get_initial(self):
        initial = super().get_initial()
        email = self.get_object()
        initial['user'] = self.request.user
        initial['category'] = Category.objects.filter(slug='otpravlennye')[0]
        initial['subject'] = f'RE: {email.subject}'
        initial['sender'] = self.request.user.email
        initial['recipients'] = email.sender
        initial['body'] = f'\n____________\n{email.body}'
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Входящие'}
        return {**context, **c_def}

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     email = queryset[0]
    #     email.read = True
    #     email.save()
    #     return queryset

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            form.save()

        return response


# Написать кому угодно, например себе от имени любого
class MailCreateView(CreateView):
    form_class = AddMailForm
    model = Email
    template_name = 'mail/add_mail.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['category'] = Category.objects.filter(slug='vhodyashie')[0]

        return initial


class DeleteMailView(DeleteView):
    model = Email
    pk_url_kwarg = 'email_pk'
    success_url = reverse_lazy('home')
