from django.urls import path
from mail.views import *


urlpatterns = [
    path('', MailSPAView.as_view(), name='index'),
]
