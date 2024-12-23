from django.urls import path
from mail.views import *


urlpatterns = [
    path('', MailListView.as_view(), name='home'),
    path('add_mail/', MailCreateView.as_view(), name='add-mail'),
    path('delete_mail/<int:email_pk>/', DeleteMailView.as_view(), name='delete-mail'),
    path('<int:email_pk>/', MailDetailView.as_view(), name='mail-body'),
    path('<slug:category_slug>/', MailListView.as_view(), name='mail-list'),
]
