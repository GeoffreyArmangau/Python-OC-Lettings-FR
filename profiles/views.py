"""Views for the profiles app: list and detail pages for user profiles."""
import logging

from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """Render the list of all profiles.

    Parameters:
        request: the HTTP request.

    Returns:
        HttpResponse rendering profiles/index.html with all Profile objects.
    """
    profiles_list = Profile.objects.all()
    logger.info("Listing %d profile(s)", profiles_list.count())
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque
# dui.
# Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it.
# Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """Render the detail page for a single profile.

    Parameters:
        request: the HTTP request.
        username: username of the User whose profile to display.

    Returns:
        HttpResponse rendering profiles/profile.html with the matching Profile.

    Raises:
        Profile.DoesNotExist: if no Profile matches username (results in a 500 error page).
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.error("Profile with username=%s does not exist", username)
        raise
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
