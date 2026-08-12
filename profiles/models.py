from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # related_name temporaire: le modèle Profile de oc_lettings_site existe encore en
    # parallèle avec la même relation vers User, ce qui provoque un conflit d'accesseur
    # inverse par défaut. Sera retiré (retour au comportement par défaut) une fois
    # l'ancien modèle supprimé, à la bascule finale.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='new_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
