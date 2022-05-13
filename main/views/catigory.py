from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from ..models import Catigory
from ..forms import CatigoryCreateForm

class CategoriesListView(LoginRequiredMixin, ListView):
	model = Catigory
	template_name = 'main/categories.html'
	context_object_name = 'categories'

class CatigoryCreateView(LoginRequiredMixin, CreateView):
	model = Catigory
	template_name = 'main/catigory_create.html'
	form_class = CatigoryCreateForm
	success_url = '/'
