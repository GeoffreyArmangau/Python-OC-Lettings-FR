"""Views for the lettings app: list and detail pages for rental listings."""
from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget
# scelerisque
def index(request):
    """Render the list of all lettings.

    Parameters:
        request: the HTTP request.

    Returns:
        HttpResponse rendering lettings/index.html with all Letting objects.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend.
# Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur lacus
# justo nec purus.
# Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in
# magna.
# Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus.
# Mauris condimentum auctor elementum.
# Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """Render the detail page for a single letting.

    Parameters:
        request: the HTTP request.
        letting_id: primary key of the Letting to display.

    Returns:
        HttpResponse rendering lettings/letting.html with the listing's title and address.

    Raises:
        Letting.DoesNotExist: if no Letting matches letting_id (results in a 500 error page).
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
