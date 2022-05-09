from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	
	path('', views.BooksListView.as_view(), name='index'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),

	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author'),
	
]