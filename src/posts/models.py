from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    tumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    #Creamos una relaciond e foreingkey para para relacionar el modelo dde author con el post
    #author = models.ForeignKey()
    
    def __str__(self):
        self.title

class Comment(models.Model):
    #user = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username


class PostView(models.Model):
    #user = models.ForeignKey()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


