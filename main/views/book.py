from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from ..models import Book
from ..forms import BookCreateForm


class BooksListView(LoginRequiredMixin, ListView):
	model = Book
	# queryset = Book.objects.filter(title__icontains='war')[:5]
	template_name = 'main/books.html'
	context_object_name = 'books'
	paginate_by = 500

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'main/book.html'
	context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	# model.added_at = 
	template_name = 'main/book_create.html'
	form_class = BookCreateForm
	def form_valid(self, form):
		form.instance.added_at = self.request.user
		return super().form_valid(form)