from django.views.generic import FormView, CreateView
from mail.forms import *


class MailSPAView(FormView):
    form_class = SimpleForm
    template_name = 'mail/index.html'
