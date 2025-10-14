from django.shortcuts import render
from django.contrib import messages
from . models import Post
from . forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'home.html', context)

def crear_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado con exito')
        
        messages.error(request, '!El formulario no es valido reintente por favor')
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'crear_post.html', context)