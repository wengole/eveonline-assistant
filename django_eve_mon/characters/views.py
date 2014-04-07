from collections import OrderedDict

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, \
    FormView

from characters.forms import ApiKeyForm, CharacterForm
from .utils import UserIsOwnerMixin
from .models import ApiKey, Character


# class AddCharacter(LoginRequiredMixin, JSONResponseMixin, TemplateView):
#     template_name = "characters/character_add.html"
#     content_type = "text/html"
#
#     def post(self, request):
#         self.content_type = "application/json"
#
#         key_id = int(request.POST.get('keyid'))
#         vcode = request.POST.get('vcode')
#         char_ids = request.POST.get('characters')
#         user = request.user
#
#         api_key, _ = ApiKey.objects.get_or_create(
#             key_id=key_id,
#             verification_code=vcode,
#             defaults={
#                 'user': user
#             }
#         )
#
#         if char_ids is not None:
#             return self.add_characters(
#                 api_key,
#                 [int(x) for x in char_ids.split(',')]
#             )
#
#         characters = api_key.get_characters()
#         context = {
#             'data': [
#                 {
#                     'id': x,
#                     'text': characters[x]['name']
#                 } for x in characters.keys()
#             ],
#         }
#         return self.render_json_response(context)
#
#     def add_characters(self, api_key, char_ids):
#         characters = api_key.get_characters()
#         for cid in char_ids:
#             char, _ = Character.objects.get_or_create(
#                 id=cid,
#                 apikey=api_key,
#                 defaults={
#                     'user': self.request.user,
#                     'name': characters[cid]['name'],
#                     'skillpoints': 0
#                 }
#             )
#             char._update_attributes()
#         return redirect(reverse('characters:manage'))

class AddCharacter(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm

    def get_form_kwargs(self):
        kwargs = super(AddCharacter, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class ManageCharacters(LoginRequiredMixin, ListView):
    model = Character

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


class UpdateCharacter(UserIsOwnerMixin, DetailView):
    model = Character

    def get(self, request, *args, **kwargs):
        character = self.get_object()
        message = character.update_character_sheet()
        messages.add_message(request, message['status'], message['text'])
        return redirect(reverse('characters:manage'))


class AddApiKey(LoginRequiredMixin, CreateView):
    model = ApiKey
    form_class = ApiKeyForm

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