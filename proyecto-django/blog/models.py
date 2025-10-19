from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha_c = models.DateField(auto_now_add=True)
    hora_c = models.TimeField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.titulo} de {self.autor}'

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_c = models.DateField(auto_now_add=True)
    hora_c = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} en el post {self.post.titulo}'

