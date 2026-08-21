"""Unit tests for the profiles app: model behavior in isolation."""
from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Profile


def create_profile(username='jdoe', favorite_city='Paris'):
    """Create and return a Profile (with its User) for use in tests."""
    user = User.objects.create_user(username=username, password='pass1234')
    return Profile.objects.create(user=user, favorite_city=favorite_city)


class ProfileModelTests(TestCase):
    """Tests for the Profile model."""

    def test_str_returns_username(self):
        """__str__ returns the associated user's username."""
        profile = create_profile(username='jdoe')
        self.assertEqual(str(profile), 'jdoe')
