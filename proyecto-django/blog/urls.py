from django.urls import path
from . import views

urlpatterns = [
    #Blog
    path('', views.home, name='home'),
    path('crear_post', views.crear_post, name='crear_post'),
    path('mis_posts/<str:user>/', views.MisPosts, name='mis_posts'),
    path('about/', views.about, name='about'),
    path('detalle/<int:id>/', views.post_detail, name='detalle'),
    path('eliminar/<int:id>/', views.post_delete, name='eliminar'),
    path('modificar/<int:id>/', views.post_edit, name='modificar'),

    #Login y registro
    path('login/', views.login1, name='login'),
    path('exit/', views.exit, name='exit'),
    path('singin/', views.singin, name='singin'),
]