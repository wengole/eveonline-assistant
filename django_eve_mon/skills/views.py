"""
Views for the Skills app
"""
from django.views.generic import ListView, FormView
from .models import Group, Skill
from .forms import AddSkillToPlanForm


class SkillsInGroups(ListView):
    """
    Browse all skills view
    """
    model = Group
