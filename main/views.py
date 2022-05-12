from django import template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Author, Book
from .forms import BookCreateForm


class BooksListView(LoginRequiredMixin, ListView):
	model = Book
	# queryset = Book.objects.filter(title__icontains='war')[:5]
	template_name = 'main/books.html'
	context_object_name = 'books'

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'main/book.html'
	context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	template_name = 'main/book_create.html'
	form_class = BookCreateForm


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

# class AuthorUpdateView(LoginRequiredMixin, UpdateView):
# 	model = User
# 	template_name = 'user/edit.html'
# 	form_class = UserUpdateForm
# 	success_url = '/users'
# 	# fields = ['username', 'groups']
# 	# form_class = UnitForm
	
# class AuthorDeleteView(DeleteView):
# 	model = User
# 	template_name = 'user/delete.html'
# 	success_url = '/users'
# 	context_object_name = 'unit'
