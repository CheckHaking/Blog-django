from typing import Any
from django.shortcuts import render, get_object_or_404, redirect

#importamos las vistas que django nos da
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#importamos los modelos que van a ser usados en las vistas
from .models import *
#Ahora traeremos los formularios a nuestro archivo de views
from .forms import PostForm, CommentForm

#parar darle funcionalidad al like de nuestro blog



class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect("detail", slug=post.slug)
        return redirect("detail", slug=self.get_object().slug)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context
    
    
    #logica para que aparezcan las vistads
    def get_object(self, **kwargs):
        
        object = super().get_object(**kwargs) #este objeto esta haciendo referencia a post create view
        if self.request.user.is_authenticated:
            #Crearemos un Post
            PostView.objects.get_or_create(user=self.request.user, post=object)
        
        return object

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


#definimos una funcion para nuestros like 
#Esta funcion la vamos a usar en nuestras urls.py para pder usarlo

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)

