from django.db import models

class Gato(models.Model):
    id = primary_key=True
    idfoto = models.CharField (
        'foto',
        max_length=10,
        )
    url = models.CharField (
        'urlgato',
        max_length=250,
        )
    ancho = models.CharField (
        'ancho',
        max_length=5000,
    )
    alto = models.CharField (
        'alto',
        max_length=5000,
    )