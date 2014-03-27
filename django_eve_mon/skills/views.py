from django.views.generic import ListView
from django_eve_mon.skills.models import Group


class SkillsList(ListView):
    queryset = Group.objects.order_by('name')
