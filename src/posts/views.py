from typing import Any
from django.shortcuts import render

#importamos las vistas que django nos da
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#importamos los modelos que van a ser usados en las vistas
from .models import *
#Ahora traeremos los formularios a nuestro archivo de views
from .forms import PostForm


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    form_class = PostForm #Cuando le pasamos form_class es lo mismo que teener el atributo fields, asi que debemos borrarlo
    model = Post
    #En nuestra vista de update, tenemos que agregar un campo mas para que funcione
    #fields = ('title','content','tumbnail','author', 'slug')
    success_url = '/' #Esta linea es para que cuando le demos submit al boton nos redirija a "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context
    
    
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    #En nuestra vista de update, tenemos que agregar un campo mas para que funcione
    #fields = ('title','content','tumbnail','author', 'slug')
    success_url = '/'#Esta linea es para que cuando le demos submit al boton nos redirija a "/"
    
    #Ahora podemos definir datos de contexto 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context
    
    
    
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/' #Esta linea es para que cuando le demos submit al boton nos redirija a "/"
