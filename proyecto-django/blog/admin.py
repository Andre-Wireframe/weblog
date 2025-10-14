from django.contrib import admin
from . models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_c']

admin.site.register(Post, PostAdmin)