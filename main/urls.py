from django.urls import path
from main.views import *
from mail.views import RedirectIndexView


urlpatterns = [
    path('', RedirectIndexView.as_view()),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
