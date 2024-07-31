from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #Tenemos que indicarle a nuestro Formulario de que modelo va a construir su estructura dentro de la clase meta 
    class Meta:
        model = Post
        fields = ('__all__')
        