from django.conf.urls import patterns, url
from .views import SkillsInGroups, AddSkillToPlan

urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=SkillsInGroups.as_view(),
        name='list'
    ),
)
