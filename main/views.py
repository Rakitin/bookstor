from django import template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Author, Book


class BooksListView(LoginRequiredMixin, ListView):
	model = Book
	# queryset = Book.objects.filter(title__icontains='war')[:5]
	template_name = 'main/index.html'
	context_object_name = 'books'

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'main/book.html'
	context_object_name = 'book'


class AuthorDetailView(LoginRequiredMixin, DetailView):
	model = Author
	template_name = 'main/author.html'
	context_object_name = 'author'
