from django.urls import path
from main.views import *
from mail.views import RedirectIndexView


urlpatterns = [
    path('mail/', RedirectIndexView.as_view()),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
