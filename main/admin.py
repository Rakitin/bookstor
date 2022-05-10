from django.contrib import admin
from .models import Book, Catigory, Author

admin.site.register(Book)
admin.site.register(Catigory)
# admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')

admin.site.register(Author, AuthorAdmin)
