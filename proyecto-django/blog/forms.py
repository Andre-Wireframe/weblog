from django.forms import ModelForm, Form
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'contenido', 'imagen']