from django.views.generic import ListView
from django_eve_mon.skills.models import Group


class SkillsInGroups(ListView):
    model = Group
