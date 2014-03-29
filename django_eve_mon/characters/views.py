from time import sleep
from braces.views import JSONResponseMixin
from django.http import HttpResponse
from django.views.generic import TemplateView


class AddCharacter(JSONResponseMixin, TemplateView):
    template_name = "characters/add_character.html"
    content_type = "text/html"

    def post(self, request):
        self.content_type = "application/json"
        context = {
            'data': [
                {'id': 123,
                 'text': 'Cpt. Failsauce'},
            ],
        }
        return self.render_json_response(context)