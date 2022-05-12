from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	
	path('', views.UsersListView.as_view(), name='users'),
	path('login', views.LoginFormView.as_view(), name='login'),
	path('logout', views.LogoutView.as_view(), name='logout'),
	path('user/<int:pk>', views.UserDetailView.as_view(), name='user'),
	path('create', views.UserCreateView.as_view(), name='user_create'),
	path('user/<int:pk>/update', views.UserUpdateView.as_view(), name='user_updeate'),
	path('user/<int:pk>/delete', views.UserDeleteView.as_view(), name='user_delete'),
]