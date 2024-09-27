from django.views.generic import FormView, CreateView
from main.forms import *


class PageNotFound(FormView):
    form_class = SimpleForm
    template_name = 'main/page404.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.status_code = 404
        return response

