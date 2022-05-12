from django.forms import ModelForm, TextInput, SelectMultiple
from django.contrib.auth.models import User

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'groups']
		
		widgets = {
			'username': TextInput(attrs={'class': 'form-control'}),
			'groups': SelectMultiple(attrs={'class': 'form-control'}),
		}
