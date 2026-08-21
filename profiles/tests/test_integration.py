"""Integration tests for the profiles app: URL routing and views (full request/response cycle)."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Profile


def create_profile(username='jdoe', favorite_city='Paris'):
    """Create and return a Profile (with its User) for use in tests."""
    user = User.objects.create_user(username=username, password='pass1234')
    return Profile.objects.create(user=user, favorite_city=favorite_city)


class ProfilesUrlTests(TestCase):
    """Tests for the profiles app URL configuration."""

    def test_index_url_resolves(self):
        """The profiles:index route maps to /profiles/."""
        self.assertEqual(reverse('profiles:index'), '/profiles/')

    def test_profile_url_resolves(self):
        """The profiles:profile route maps to /profiles/<username>/."""
        self.assertEqual(reverse('profiles:profile', args=['jdoe']), '/profiles/jdoe/')


class ProfilesViewTests(TestCase):
    """Tests for the profiles app views."""

    def setUp(self):
        """Create a profile available to every test in this class."""
        self.profile = create_profile(username='jdoe')

    def test_index_view_status_code_and_template(self):
        """The index view returns 200, uses the right template and lists the profile."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn(self.profile, response.context['profiles_list'])

    def test_profile_view_status_code_and_context(self):
        """The profile view returns 200, uses the right template and context."""
        response = self.client.get(reverse('profiles:profile', args=[self.profile.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_profile_view_missing_profile_raises(self):
        """An unknown username raises Profile.DoesNotExist (unhandled -> 500 in production)."""
        with self.assertRaises(Profile.DoesNotExist):
            self.client.get(reverse('profiles:profile', args=['nobody']))
