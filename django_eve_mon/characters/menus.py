from django.core.urlresolvers import reverse

from menu import Menu, MenuItem
from .models import Character


def profile_title(request):
    """
    Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return '%s\'s Profile' % name


def characters(request):
    return [
        MenuItem(
            character.name,
            character.get_absolute_url()
        ) for character in Character.objects.filter(user=request.user)
    ]


Menu.add_item(
    'Characters',
    MenuItem(
        title='',
        url='',
        children=characters
    )

)
