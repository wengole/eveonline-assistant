from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView


class AddPlan(LoginRequiredMixin, CreateView):
    pass


class ManagePlans(LoginRequiredMixin, UpdateView):
    pass


class PlanDetail(LoginRequiredMixin, DetailView):
    pass