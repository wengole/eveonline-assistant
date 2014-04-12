from django.core.urlresolvers import reverse

from menu import Menu, MenuItem


def skills_menu(request):
    menu = []
    menu.append(
        MenuItem(
            title='Skills',
            url='#',
            classes='dropdown-header',
        )
    )
    return menu


Menu.add_item(
    'top_nav_left',
    MenuItem(
        title='Browse all skills',
        url=reverse('skills:list'),
        weight=3
    )
)
