from django.urls import path
from mail.views import *


urlpatterns = [
    path('', MailListView.as_view(), name='index'),
    path('mail/<slug:category_slug>/', MailListView.as_view(), name='mail-list'),
    path('mail/<int:email_pk>/', MailDetailView.as_view(), name='mail-body'),
    path('add_mail/', MailCreateView.as_view(), name='add_mail'),
]
