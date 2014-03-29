from time import sleep
from braces.views import JSONResponseMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from evelink.account import Account
from evelink.api import API
from evelink.eve import EVE


class AddCharacter(JSONResponseMixin, TemplateView):
    template_name = "characters/add_character.html"
    content_type = "text/html"

    def post(self, request):
        self.content_type = "application/json"

        key_id = int(request.POST.get('keyid'))
        vcode = request.POST.get('vcode')
        characters = self.get_characters_from_api(key_id, vcode)
        context = {
            'data': characters,
        }
        return self.render_json_response(context)

    def get_characters_from_api(self, key_id, vcode):
        api = API(api_key=(key_id, vcode))
        account = Account(api=api)
        characters = account.characters()[0]
        return [
            {
                'id': x,
                'text': characters[x]['name']
            } for x in characters.keys()
        ]
