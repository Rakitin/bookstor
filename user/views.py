# from django.urls import reverse

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserUpdateForm

class LoginFormView(FormView):
	form_class = AuthenticationForm
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
	template_name = 'user/users.html'
	context_object_name = 'users'

class UserDetailView(LoginRequiredMixin, DetailView):
	model = User
	template_name = 'user/user.html'
	context_object_name = 'user_info'

class UserCreateView(LoginRequiredMixin, FormView):
	form_class = UserCreationForm
	success_url = '/users'
	template_name = 'user/create.html'
	def form_valid(self, form):
		form.save()
		return super(UserCreateView, self).form_valid(form)


# class UserCreateView(LoginRequiredMixin, CreateView):
# 	model = User
# 	# model.password
# 	template_name = 'user/edit.html'
# 	fields = ['username', 'password', 'groups']
# 	success_url = '/users'
# 	# success_url = reverse('users')
	
# 	# form_class = UnitForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'user/edit.html'
	form_class = UserUpdateForm
	success_url = reverse_lazy('users')
	# fields = ['username', 'groups']
	# form_class = UnitForm
	
class UserDeleteView(DeleteView):
	model = User
	template_name = 'user/delete.html'
	success_url = reverse_lazy('users')
	context_object_name = 'user_info'
