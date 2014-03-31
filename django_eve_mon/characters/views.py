from braces.views import JSONResponseMixin, LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.views.generic import TemplateView, ListView, DetailView
from evelink.account import Account
from evelink.api import API
from django_eve_mon.skills.models import Group

from .models import ApiKey, Character


class AddCharacter(LoginRequiredMixin, JSONResponseMixin, TemplateView):
    template_name = "characters/character_add.html"
    content_type = "text/html"

    def post(self, request):
        self.content_type = "application/json"

        key_id = int(request.POST.get('keyid'))
        vcode = request.POST.get('vcode')
        char_ids = request.POST.get('characters')
        user = request.user

        if char_ids is not None:
            return self.add_characters(
                key_id,
                vcode,
                [int(x) for x in char_ids.split(',')],
                user
            )

        characters = self.get_characters_from_api(key_id, vcode)
        context = {
            'data': [
                {
                    'id': x,
                    'text': characters[x]['name']
                } for x in characters.keys()
            ],
        }
        return self.render_json_response(context)

    def get_characters_from_api(self, key_id, vcode):
        api = API(api_key=(key_id, vcode))
        account = Account(api=api)
        return account.characters()[0]

    def add_characters(self, key_id, vcode, char_ids, user):
        characters = self.get_characters_from_api(key_id, vcode)
        api_key, _ = ApiKey.objects.get_or_create(
            key_id=key_id,
            verification_code=vcode,
            defaults={
                'user': user
            }
        )
        for cid in char_ids:
            char, _ = Character.objects.get_or_create(
                id=cid,
                apikey=api_key,
                defaults={
                    'user': user,
                    'name': characters[cid]['name'],
                    'skillpoints': 0
                }
            )
        return redirect(reverse('characters:manage'))


class ManageCharacters(LoginRequiredMixin, ListView):
    model = Character


class FetchSkills(LoginRequiredMixin, ListView):
    model = Character


class ManageApiKeys(LoginRequiredMixin, ListView):
    model = ApiKey


class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        character = self.get_object()
        context = {
            'object_type': character._meta.model_name,
            'group_list': Group.objects.all()
        }
        return super(CharacterDetail, self).get_context_data(**context)