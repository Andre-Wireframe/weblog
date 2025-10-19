#De vistas
from django.shortcuts import render, redirect, get_list_or_404

#Vistas y decoraciones
from django.contrib import messages

#Login y singin
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Parte del proyecto
from . models import Post
from . forms import PostForm, Registro

# Create your views here.

#Login y registro

def exit(request):
    logout(request)
    return redirect('home')

def singin(request):
    form = Registro()
    if request.method == 'POST':
        form = Registro(data = request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password1']
            user = authenticate(username = usuario, password = contraseña)
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('home')
        
        else:
            try:
                comp = form.data['username']
                uses = User.objects.get(username = comp)
                messages.error(request, '!El usuario ya existe pruebe con otro')
            except:
                messages.error(request, '!El formulario no es valido, pruebe usar una contraseña mas compleja y verifique que las contraseñas coincidan')
        form = Registro()
    return render(request, 'registration/singin.html', {'form':form})

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            user = authenticate(username = usuario, password = contraseña)
            if user is not None:
                login(request, user)
                messages.success(request, 'Sesion iniciada con exito')
                return redirect('home')
            else:
                messages.error(request, '!El ususario o contraseña no son correctos')
        else:
            messages.error(request, '!El formulario es invalido')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})

#Vistas de blog

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def crear_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado con exito')
            return redirect('home')
        
        messages.error(request, '!El formulario no es valido reintente por favor')
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'crear_post.html', context)

@login_required
def MisPosts(request, user):

    posts = get_list_or_404(Post, autor = user)

    context = {
        'posts':posts,
    }

    return render(request, 'mis_posts.html', context)