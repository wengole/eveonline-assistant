from collections import OrderedDict

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, \
    FormView

from .forms import ApiKeyForm, CharacterForm
from .utils import UserIsOwnerMixin
from .models import ApiKey, Character


class AddCharacter(LoginRequiredMixin, FormView):
    form_class = CharacterForm
    template_name = 'characters/character_form.html'

    def get_form_kwargs(self):
        kwargs = super(AddCharacter, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        for character in form.cleaned_data['char_ids']:
            character.enabled = True
            character.save()
        self.success_url = form.cleaned_data['char_ids'][0].get_absolute_url()
        return super(AddCharacter, self).form_valid(form)


class ManageCharacters(LoginRequiredMixin, ListView):
    model = Character

    def get_queryset(self):
        queryset = self.model.objects.filter(
            user=self.request.user,
            enabled=True
        )
        return queryset


class UpdateCharacter(UserIsOwnerMixin, DetailView):
    model = Character

    def get(self, request, *args, **kwargs):
        character = self.get_object()
        if not character.enabled:
            raise Http404
        message = character.update_character_sheet()
        messages.add_message(request, message['status'], message['text'])
        return redirect(reverse_lazy('characters:manage'))


class AddApiKey(LoginRequiredMixin, CreateView):
    model = ApiKey
    form_class = ApiKeyForm
    success_url = reverse_lazy('characters:add')

    def get_form_kwargs(self):
        kwargs = super(AddApiKey, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddApiKey, self).form_valid(form)


class ManageApiKeys(LoginRequiredMixin, ListView):
    model = ApiKey

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


class CharacterDetail(UserIsOwnerMixin, DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        character = self.get_object()
        if not character.enabled:
            raise Http404
        skills_list = character.skilltrained_set.select_related().order_by(
            'skill__group',
            'skill__name')
        groups = OrderedDict()
        for skill in skills_list:
            if skill.skill.group.name not in groups:
                groups[skill.skill.group.name] = []
            groups[skill.skill.group.name].append(skill)
        context = {
            'groups': groups
        }
        return super(CharacterDetail, self).get_context_data(**context)