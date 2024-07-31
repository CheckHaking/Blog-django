from django.db import models

#Despues de configurar el django-allauth, vamos a crear nuestro modelo de usuario
from django.contrib.auth.models import AbstractUser

#Para usar reverse
from django.shortcuts import reverse



class User(AbstractUser):
    #AbstractUser se encarga de lo que es username, password, email y especificar cualqiier otra cosa que querramos
    pass

    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    tumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    #Creamos una relaciond e foreingkey para para relacionar el modelo dde author con el post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Para usar el slug en url hay que darselo en el modelo
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.title
    
        #Para usar los links de cada carta con el post, y que nos lleve a abrir los detalles de cada carta, definimos una funcion que obtenga la url absoluta
    
    def get_absolute_url(self):
        print(f"slug:{self.slug}")
        return reverse("detail", kwargs={
            "slug": self.slug
            })
        
    @property
    def get_comment_cout(self):
        return self.comment_set.all().count()
        
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()
    
    
    
        

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    



class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user.username
    

    
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user.username

