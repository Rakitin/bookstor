from django.forms import ModelForm, TextInput
from ..models import Catigory

class CatigoryCreateForm(ModelForm):
	class Meta:
		model = Catigory
		fields = ['name']
		
		widgets = {
			'name': TextInput(attrs={'class': 'form-control'}),
		}

