from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from . import forms
from . import models

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        return super(SignUpView, self).form_valid(form)


class IndexView(TemplateView):
    template_name = 'index.html'
