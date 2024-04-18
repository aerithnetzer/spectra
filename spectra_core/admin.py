from django.contrib import admin
from .models import Author, Author_Links, Keyword, Work

admin.site.register(Author)
admin.site.register(Author_Links)
admin.site.register(Keyword)
admin.site.register(Work)