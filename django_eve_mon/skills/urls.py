from django.conf.urls import patterns, url
from .views import SkillsList

urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=SkillsList.as_view(),
        name='list'
    ),
)
