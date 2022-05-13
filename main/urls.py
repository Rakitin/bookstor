from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	
	path('', views.BooksListView.as_view(), name='index'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
	path('book/create', views.BookCreateView.as_view(), name='book_create'),

	path('authors/', views.AuthorsListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author'),
	path('author/create', views.AuthorCreateView.as_view(), name='author_create'),
	# path('author/<int:pk>/update', views.UserUpdateView.as_view(), name='author_updeate'),
	# path('author/<int:pk>/delete', views.UserDeleteView.as_view(), name='author_delete'),

	path('categories/', views.CategoriesListView.as_view(), name='categories'),
	path('catigory/create', views.CatigoryCreateView.as_view(), name='catigory_create'),


]