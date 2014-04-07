from django.core.urlresolvers import reverse

from menu import Menu, MenuItem
from .models import Character


def characters(request):
    return [
        MenuItem(
            title=character.name,
            url=character.get_absolute_url()
        ) for character in Character.objects.filter(
            user=request.user,
            enabled=True
        )
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
            title='Add API Key',
            url=reverse('characters:add_api')
        )
    )
    menu.append(
        MenuItem(
            title='Manage API Keys',
            url=reverse('characters:manage_apis')
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
        check=lambda r: r.user.is_authenticated()
    )

)
