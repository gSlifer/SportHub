from django import forms
from .models import Recinto, Comment

class RecintoForm(forms.ModelForm):
    """
    Formulario para el modelo Recinto.
    
    Este formulario se utiliza para crear y actualizar instancias del modelo Recinto.
    Incluye los campos 'name', 'adress', 'phone', 'email', 'sport', 'schedule' y 'rating'.
    """
    class Meta:
        model = Recinto
        fields = ['name', 'adress', 'phone', 'email', 'sport', 'schedule']

class CommentForm(forms.ModelForm):
    """
    Formulario para el modelo Comentario.
    
    Este formulario se utiliza para crear instancias del modelo Comentario.
    Incluye los campos 'text' y 'label'.
    """
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comentario'}
