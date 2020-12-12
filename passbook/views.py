from django.shortcuts import render
from django.views.generic import View

from pdj.views import BaseView

# Create your views here.


class PassBookView(BaseView, View):
    template_name = 'passbook/index.html'

    def get(self, request, *args, **kwargs):

        return self.response(request, self.template_name, {})
