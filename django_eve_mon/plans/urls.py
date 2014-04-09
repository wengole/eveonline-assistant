from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^add/$',
        view=views.AddPlan.as_view(),
        name='add'
    ),
    url(
        regex=r'^manage/$',
        view=views.ManagePlans.as_view(),
        name='manage'
    ),
    url(
        regex=r'^manage/(?P<plan_id>\d+)/$',
        view=views.PlanDetail.as_view(pk_url_kwarg='plan_id'),
        name='detail'
    ),
    url(
        regex=r'^addToPlan/$',
        view=views.AddSkillToPlan.as_view(),
        name='add_to_plan'
    ),
)
