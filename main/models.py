from django.urls import reverse
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	description = models.TextField(verbose_name='Описание')
	isbn = models.CharField(max_length=13)
	# img = models.ImageField()

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	catigory = models.ManyToManyField('Catigory', verbose_name='Категория')
	author = models.ManyToManyField('Author', verbose_name='Автор')

	added_at = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('book', args=[str(self.pk)])

	def __str__(self) :
		return self.title

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'


class Catigory(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название')

	def __str__(self) :
		return self.name
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Author(models.Model):
	first_name = models.CharField(max_length=100, verbose_name='Имя')
	last_name = models.CharField(max_length=100, verbose_name='Фамилия')

	# photo = models.ImageField()

	def get_absolute_url(self):
		return reverse('author', args=[str(self.pk)])

	def __str__(self) :
		return '{0} {1}'.format(self.last_name, self.first_name)

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'
