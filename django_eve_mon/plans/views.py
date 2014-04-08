"""
Views for the Plans app
"""
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Plan
from .forms import PlanForm
from skills.models import Group


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


class ManagePlans(LoginRequiredMixin, UpdateView):
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