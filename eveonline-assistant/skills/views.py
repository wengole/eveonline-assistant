"""
Views for the Skills app
"""
from django.views.generic import ListView

from .models import Group


class SkillsInGroups(ListView):
    """
    Browse all skills view
    """
    model = Group
