from django.core.urlresolvers import reverse

from menu import Menu, MenuItem


def plans(request):
    return [
        MenuItem(
            title=plan.name,
            url=plan.get_absolute_url(),
        ) for plan in request.user.plan_set.all()
    ]


def plans_menu(request):
    menu = []
    plns = plans(request)
    menu.append(
        MenuItem(
            title='Plans',
            url='#',
            classes='dropdown-header',
        )
    )
    menu.extend(plns)
    menu.append(
        MenuItem(
            title='divider',
            url='',
            classes='divider'
        )
    )
    menu.append(
        MenuItem(
            title='Add Plan',
            url=reverse('plans:add')
        )
    )
    menu.append(
        MenuItem(
            title='Manage Plans',
            url=reverse('plans:manage')
        )
    )
    return menu


Menu.add_item(
    'top_nav_left',
    MenuItem(
        title='Plans',
        url='#',
        children=plans_menu,
        classes='dropdown',
        check=lambda r: r.user.is_authenticated(),
        weight=2
    )
)
