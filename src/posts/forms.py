from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    #Tenemos que indicarle a nuestro Formulario de que modelo va a construir su estructura dentro de la clase meta 
    class Meta:
        model = Post
        fields = ('__all__')


class CommentForm(forms.ModelForm):
    
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content', )
        