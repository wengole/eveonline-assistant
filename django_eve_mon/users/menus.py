from django.core.urlresolvers import reverse
from menu import Menu, MenuItem


def profile_title(request):
    """
    Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return '%s' % name


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