from django.contrib.auth.forms import AuthenticationForm
from django import forms

class MyAuthenticationForm(AuthenticationForm):
	username = forms.CharField(label="Имя", max_length=30, attrs='')
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
