from django.conf.urls import patterns, url
from .views import AddCharacter, ManageCharacters

urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^add/$',
        view=AddCharacter.as_view(),
        name='add'
    ),
    url(
        regex=r'^manage/$',
        view=ManageCharacters.as_view(),
        name='manage'
    ),
)
