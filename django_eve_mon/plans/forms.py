"""
Forms for the Plans app
"""
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Fieldset
from django.forms import ModelForm
from .models import Plan


class PlanForm(ModelForm):
    """
    Simple form to add a new Skill Plan
    """

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                'Add new skill plan',
                'name',
                'character'
            ),
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

        self.fields['character'].empty_label = ''

    class Meta:
        """
        Form settings
        """
        model = Plan
        exclude = ['user', ]
