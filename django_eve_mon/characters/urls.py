from django.conf.urls import patterns, url
from .views import AddCharacter, ManageCharacters, ManageApiKeys, CharacterDetail, UpdateCharacter

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
    url(
        regex=r'^manage/(?P<char_id>\d+)/fetch/$',
        view=UpdateCharacter.as_view(pk_url_kwarg='char_id'),
        name='fetch'
    ),
    url(
        regex=r'^manage/(?P<char_id>\d+)/$',
        view=CharacterDetail.as_view(pk_url_kwarg='char_id'),
        name='detail'
    ),
    url(
        regex=r'^apis/manage/$',
        view=ManageApiKeys.as_view(),
        name='manage-apis'
    ),
)
