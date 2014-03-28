from django.views.generic import ListView
from .models import Group


class SkillsInGroups(ListView):
    model = Group
