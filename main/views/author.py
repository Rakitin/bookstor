from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Author


class AuthorsListView(LoginRequiredMixin, ListView):
	model = Author
	template_name = 'main/authors.html'
	context_object_name = 'authors'

class AuthorDetailView(LoginRequiredMixin, DetailView):
	model = Author
	template_name = 'main/author.html'
	context_object_name = 'author'

class AuthorCreateView(LoginRequiredMixin, CreateView):
	model = Author
	template_name = 'main/author_edit.html'
	fields = ['first_name', 'last_name']
	# form_class = UnitForm

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
	pass
# 	model = User
# 	template_name = 'user/edit.html'
# 	form_class = UserUpdateForm
# 	success_url = '/users'
# 	# fields = ['username', 'groups']
# 	# form_class = UnitForm
	
class AuthorDeleteView(DeleteView):
	pass
# 	model = User
# 	template_name = 'user/delete.html'
# 	success_url = '/users'
# 	context_object_name = 'unit'
