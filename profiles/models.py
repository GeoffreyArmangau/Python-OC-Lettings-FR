"""Database models for the profiles app: user profile extension data."""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extra profile data attached one-to-one to a Django User.

    user: the associated auth.User (one Profile per User).
    favorite_city: optional free-text favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the associated user's username."""
        return self.user.username
