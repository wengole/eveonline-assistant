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
    url(
        regex=r'^addToPlan/(?P<skill_id>\d+)/$',
        view=AddSkillToPlan.as_view(),
        name='add_to_plan'
    ),
)
