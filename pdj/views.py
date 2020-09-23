# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View


class BaseView(LoginRequiredMixin):

    def response(self, request, template_name, contents):
        template = loader.get_template(template_name)
        return HttpResponse(template.render(contents, request))


class HomeView(BaseView, View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return self.response(request, self.template_name, None)
