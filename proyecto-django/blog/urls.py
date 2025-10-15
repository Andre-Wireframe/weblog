from django.urls import path
from . import views

urlpatterns = [
    #Blog
    path('', views.home, name='home'),
    path('crear_post', views.crear_post, name='crear_post'),

    #Login y registro
    path('login/', views.login1, name='login'),
    path('exit/', views.exit, name='exit'),
    path('singin/', views.singin, name='singin'),
]