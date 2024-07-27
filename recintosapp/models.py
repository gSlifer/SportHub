from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Modelo de usuario.
    Cada usuario tiene un usuario de Django pero además el atributo is_admin que sirve para saber
    si puede hacer modificaciones a los recintos.
    """
    is_admin = models.BooleanField(default=False) #Es o no usuario admin.
   

class Recinto(models.Model):
    """
    Modelo de recinto.
    Cada recinto tiene un nombre, una dirección, un teléfono, un correo electrónico, una lista de deportes disponibles, 
    un horario y una valoración.
    """
    name = models.CharField(max_length=50) #Nombre del recinto.
    adress = models.CharField(max_length=50) #Dirección del recinto.
    phone = models.CharField(max_length=50) #Teléfono del recinto.
    email = models.EmailField() #Correo electrónico del recinto.
    sports = [('futbol', 'Fútbol'),('baloncesto', 'Baloncesto'),('tenis', 'Tenis'),('padel', 'Pádel'),
    ('voleibol', 'Voleibol'),('otro', 'Otro')]#Lista de deportes.
    sport = models.CharField(max_length=20,choices=sports) #Deporte seleccionado.
    schedule = models.CharField(max_length=50) #Horario de funcionamiento del recinto.
    rating = models.FloatField(default=0) #Valoración del recinto.
    rating_counter = models.IntegerField(default=0) 
    def __str__(self):
        """
        Devuelve el nombre del recinto cuando se imprime el objeto.
        """
        return self.name
    
class Comment(models.Model):
    """
    Modelo de comentario.
    Cada comentario tiene un usuario emisor, una recinto sobre el cual comento, el texto del comentario
    y una fecha en la que se realizó el comentario.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recinto.name}'