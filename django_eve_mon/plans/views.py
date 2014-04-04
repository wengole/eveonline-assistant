from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Plan
from .forms import PlanForm


class AddPlan(LoginRequiredMixin, CreateView):
    model = Plan
    form_class = PlanForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPlan, self).form_valid(form)


class ManagePlans(LoginRequiredMixin, UpdateView):
    model = Plan


class PlanDetail(LoginRequiredMixin, DetailView):
    model = Plan