"""
Forms for the Plans app
"""
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Reset
from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    """
    Simple ModelForm to add a new Skill Plan
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
                Submit('save', 'Add', css_class='btn btn-success'),
                Reset('reset', 'Reset', css_class='btn btn-default')
            )
        )

        self.fields['character'].empty_label = ''

    class Meta:
        """
        Form settings
        """
        model = Plan
        exclude = ['user', ]


class AddSkillToPlanForm(forms.Form):
    """
    Simple plain form to add a skill to a plan
    """

    def __init__(self, *args, **kwargs):
        super(AddSkillToPlanForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'


