from django.http import HttpResponse
from django.views.generic import TemplateView


class AddCharacter(TemplateView):
    template_name = "characters/add_character.html"

    def post(self, request):
        return HttpResponse('POSTed')