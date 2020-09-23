# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views import generic

from pdj.views import BaseView

from .forms import LoginForm, SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class LogoutView(views.LogoutView):
    template_name = 'registration/logged_out.html'


class UserSettingView(BaseView, generic.View):

    template_name = 'account/setting.html'

    def get(self, request, *args, **kwargs):
        return self.response_with_breadcrumb(request, self.template_name, {})
