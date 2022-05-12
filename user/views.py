# from django.urls import reverse

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# from .forms import MyAuthenticationForm

class LoginFormView(FormView):
	form_class = AuthenticationForm
	# form_class = MyAuthenticationForm
	template_name = "user/login.html"
	success_url = "/"
	def form_valid(self, form):
		self.user = form.get_user()
		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
		
class UsersListView(LoginRequiredMixin, ListView):
	model = User
	template_name = 'user/index.html'
	context_object_name = 'users'

class UserDetailView(LoginRequiredMixin, DetailView):
	model = User
	template_name = 'user/user.html'
	context_object_name = 'user_info'

class UserCreateView(LoginRequiredMixin, CreateView):
	model = User
	# model.password
	template_name = 'user/edit.html'
	fields = ['username', 'password', 'groups']
	success_url = '/users'
	# success_url = reverse('users')
	
	# form_class = UnitForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'user/edit.html'
	# form_class = UnitForm
	
class UserDeleteView(DeleteView):
	model = User
	template_name = 'user/delete.html'
	success_url = '/users'
	context_object_name = 'unit'
