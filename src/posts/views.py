from django.shortcuts import render

#importamos las vistas que django nos da
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#importamos los modelos que van a ser usados en las vistas
from .models import *


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    #En nuestra vista de update, tenemos que agregar un campo mas para que funcione
    fields = ('title','content','tumbnail','author', 'slug')
    
    
    
class PostUpdateView(UpdateView):
    model = Post
    #En nuestra vista de update, tenemos que agregar un campo mas para que funcione
    fields = ('title','content','tumbnail','author', 'slug')
    
    
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
