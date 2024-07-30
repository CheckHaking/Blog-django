from django.db import models

#Despues de configurar el django-allauth, vamos a crear nuestro modelo de usuario
from django.contrib.auth.models import AbstractUser



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

