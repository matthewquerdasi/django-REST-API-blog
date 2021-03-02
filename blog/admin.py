from django.contrib import admin
from . import models

# register two models in models.py (to make available on admin page)
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category)


