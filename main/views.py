from django import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book


class BooksListView(ListView):
	model = Book
	template_name = 'main/index.html'
	context_object_name = 'books'

class BookDetailView(DetailView):
	model = Book
	template_name = 'main/book.html'
	context_object_name = 'book'


class AuthorDetailView(DetailView):
	model = Author
	template_name = 'main/author.html'
	context_object_name = 'author'
