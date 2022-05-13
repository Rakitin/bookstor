from django.forms import ModelForm, TextInput, Textarea, SelectMultiple
from ..models import Book

class BookCreateForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'description', 'isbn', 'catigory', 'author']
		
		widgets = {
			'title': TextInput(attrs={'class': 'form-control'}),
			'description': Textarea(attrs={'class': 'form-control'}),
			'isbn': TextInput(attrs={'class': 'form-control'}),
			'catigory': SelectMultiple(attrs={'class': 'form-control'}),
			'author': SelectMultiple(attrs={'class': 'form-control'}),
		}

