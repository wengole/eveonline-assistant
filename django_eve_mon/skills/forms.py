from crispy_forms.helper import FormHelper
from django.forms import forms


class AddSkillToPlanForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AddSkillToPlanForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'


