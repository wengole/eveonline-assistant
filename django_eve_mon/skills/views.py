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


class AddSkillToPlan(FormView):
    form_class = AddSkillToPlanForm
    template_name = 'skills/add_to_plan.html'

    def get_context_data(self, **kwargs):
        context = super(AddSkillToPlan, self).get_context_data(**kwargs)
        skill = None
        try:
            skill = Skill.objects.get(id=self.kwargs.get('skill_id', 0))
        except Skill.DoesNotExist:
            pass
        context.update({
            'skill': skill
        })
        return context