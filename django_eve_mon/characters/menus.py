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

    return '%s' % name


def characters(request):
    return [
        MenuItem(
            title=character.name,
            url=character.get_absolute_url()
        ) for character in Character.objects.filter(user=request.user)
    ]


def characters_menu(request):
    menu = []
    menu.append(
        MenuItem(
            title='Characters',
            url='#',
            classes='dropdown-header',
        )
    )
    menu.extend(characters(request))
    menu.append(
        MenuItem(
            title='divider',
            url='',
            classes='divider'
        )
    )
    menu.append(
        MenuItem(
            title='Add Character',
            url=reverse('characters:add')
        )
    )
    menu.append(
        MenuItem(
            title='Manage Characters',
            url=reverse('characters:manage')
        )
    )
    menu.append(
        MenuItem(
            title='divider',
            url='',
            classes='divider'
        )
    )
    menu.append(
        MenuItem(
            title='API Keys',
            url='#',
            classes='dropdown-header',
        )
    )
    menu.append(
        MenuItem(
            title='Manage API Keys',
            url=reverse('characters:manage-apis')
        )
    )
    return menu


def profile_menu(request):
    menu = []
    menu.append(
        MenuItem(
            title=profile_title,
            url='#',
            classes='dropdown-header'
        )
    )
    menu.append(
        MenuItem(
            title='Update My Info',
            url=reverse('users:update'),
        )
    )
    menu.append(
        MenuItem(
            title='Manage E-Mail Addresses',
            url=reverse('account_email')
        )
    )
    return menu

Menu.add_item(
    'top_nav_left',
    MenuItem(
        title='Characters',
        url='#',
        children=characters_menu,
        classes='dropdown',
        check=lambda request: request.user.is_authenticated()
    )

)

Menu.add_item(
    'top_nav_right',
    MenuItem(
        title=profile_title,
        url='#',
        children=profile_menu,
        classes='dropdown',
        check=lambda request: request.user.is_authenticated()
    )
)
Menu.add_item(
    'top_nav_right',
    MenuItem(
        title='Logout',
        url=reverse('account_logout'),
        check=lambda request: request.user.is_authenticated()
    )
)
Menu.add_item(
    'top_nav_right',
    MenuItem(
        title='Sign Up',
        url=reverse('account_signup'),
        check=lambda request: request.user.is_anonymous()
    )
)