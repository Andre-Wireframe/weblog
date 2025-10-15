from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'contenido', 'imagen']

class Registro(UserCreationForm):
    pass
