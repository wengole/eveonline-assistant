"""
Views for the Plans app
"""
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, FormView

from .models import Plan, PlannedSkill
from .forms import PlanForm, AddSkillToPlanForm
from skills.models import Group, Skill


class AddPlan(LoginRequiredMixin, CreateView):
    """
    Add a plan
    """
    model = Plan
    form_class = PlanForm

    def form_valid(self, form):
        """
        AdSet user of Plan instance to current user
        :param form: Passed in by Django
        """
        form.instance.user = self.request.user
        return super(AddPlan, self).form_valid(form)


class ManagePlans(LoginRequiredMixin, ListView):
    """
    List plans
    """
    model = Plan


class PlanDetail(LoginRequiredMixin, DetailView):
    """
    Edit a plan
    """
    model = Plan

    def get_context_data(self, **kwargs):
        """
        Add groups (and therefore skills) to plan detail for skill browser
        :param kwargs: Passed in by Django
        """
        context = super(PlanDetail, self).get_context_data(**kwargs)
        context.update({
            'group_list': Group.objects.all()
        })
        return context


class AddSkillToPlan(LoginRequiredMixin, FormView):
    model = PlannedSkill
    form_class = AddSkillToPlanForm
    template_name = 'plans/add_to_plan.html'

    def get_initial(self):
        initial = super(AddSkillToPlan, self).get_initial()
        plan = Plan.objects.get(pk=self.request.REQUEST.get('plan'))
        skill = Skill.objects.get(pk=self.request.REQUEST.get('skill'))
        initial.update({
            'plan': plan,
            'skill': skill
        })
        return initial

    def form_valid(self, form):
        plan = form.cleaned_data['plan']
        plan.add_to_plan(
            skill=form.cleaned_data['skill'],
            level=form.cleaned_data['level']
        )
        return super(AddSkillToPlan, self).form_valid(form)

    def get_success_url(self):
        return reverse('plans:detail', args=[self.request.POST['plan']])

