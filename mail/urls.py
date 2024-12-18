from django.urls import path
from mail.views import *


urlpatterns = [
    # path('', RedirectIndexView.as_view()),
    path('', MailListView.as_view(), name='home'),
    path('<int:email_pk>/', MailDetailView.as_view(), name='mail-body'),
    path('<slug:category_slug>/', MailListView.as_view(), name='mail-list'),
    path('add_mail/', MailCreateView.as_view(), name='add_mail'),
]
