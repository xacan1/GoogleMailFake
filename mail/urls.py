from django.urls import path
from mail.views import *


urlpatterns = [
    path('', RedirectIndexView.as_view(), name='index'),
    path('mail/', MailListView.as_view(), name='home'),
    path('mail/<int:email_pk>/', MailDetailView.as_view(), name='mail-body'),
    path('mail/<slug:category_slug>/', MailListView.as_view(), name='mail-list'),
    path('mail/add_mail/', MailCreateView.as_view(), name='add_mail'),
]
