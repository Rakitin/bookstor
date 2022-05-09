from tabnanny import verbose
from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	isbn = models.CharField(max_length=13)
	# img = models.ImageField()

	catigory = models.ManyToManyField('Catigory')
	author = models.ManyToManyField('Author')

	def __str__(self) :
		return self.title


class Catigory(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название')

	def __str__(self) :
		return self.name

class Author(models.Model):
	first_name = models.CharField(max_length=100, verbose_name='Имя')
	last_name = models.CharField(max_length=100, verbose_name='Фамилия')

	def __str__(self) :
		return '{0} {1}'.format(self.last_name, self.first_name)

	class Meta:
		verbose_name = 'Автор'