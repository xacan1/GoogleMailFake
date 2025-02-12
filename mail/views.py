from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from mail.forms import *
from mail.models import *
import mail.service as service


class RedirectIndexView(RedirectView):
    permanent = True
    url = reverse_lazy('home')


class MailListView(LoginRequiredMixin, FormView, ListView):
    form_class = AddMailForm
    template_name = 'mail/index.html'
    paginate_by = 50
    login_url = reverse_lazy('login')
    context_object_name = 'emails'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        query_search = self.request.GET.get('q', '')
        slug = self.kwargs.get('category_slug', '')

        if query_search:
            queryset = service.search_email(query_search)
        else:
            queryset = service.get_emails_by_category(self.request.user, slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('category_slug', '')
        c_def = {'title': '', }
        c_def = {'query_search': self.request.GET.get('q', '')}

        if slug:
            queryset = Category.objects.filter(slug=slug)

            if queryset:
                category = queryset[0]
                c_def = {'title': f'{category.name} - {self.request.user}'}

        # c_def['emails'] = self.get_emails()

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
    pk_url_kwarg = 'email_pk'
    context_object_name = 'email'
    login_url = reverse_lazy('login')

    def get_template_names(self):
        template_names = super().get_template_names()
        email = self.get_object()
        have_chain = service.have_chain(email.pk)

        if have_chain:
            template_names.append('mail/body_mail_chain.html')
        else:
            template_names.append('mail/body_mail.html')

        return template_names

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
        initial['parent'] = email.pk
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Входящие'}
        email = self.get_object()
        chain_emails = service.get_chain(email.pk)
        c_def['chain_emails'] = chain_emails
        c_def['attachments'] = Attachment.objects.filter(email=email)
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
    model = Email
    form_class = AddMailForm
    template_name = 'mail/add_mail.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['category'] = Category.objects.filter(slug='vhodyashie')[0]

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = AddFilesFromSet(self.request.POST,
                                                 self.request.FILES)
        else:
            context['formset'] = AddFilesFromSet()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()  # Сохраняем основной объект
            formset.instance = self.object
            formset.save()  # Сохраняем файлы
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DeleteMailView(DeleteView):
    model = Email
    pk_url_kwarg = 'email_pk'
    success_url = reverse_lazy('home')
