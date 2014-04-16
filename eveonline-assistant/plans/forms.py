"""
Forms for the Plans app
"""
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Reset, Field
from django import forms
from django.core.urlresolvers import reverse

from characters.models import Character
from .models import Plan, PlannedSkill
from skills.models import Skill


class PlanForm(forms.ModelForm):
    """
    Simple ModelForm to add a new Skill Plan
    """

    def __init__(self, user, *args, **kwargs):
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
        self.fields['character'].queryset = user.characters.filter(enabled=True)

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
    plan = forms.ModelChoiceField(
        queryset=Plan.objects
    )
    skill = forms.ModelChoiceField(
        queryset=Skill.objects
    )
    level = forms.IntegerField(
        min_value=1,
        max_value=5
    )

    def __init__(self, *args, **kwargs):
        super(AddSkillToPlanForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = reverse('plans:add_to_plan')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.render_hidden_fields = True
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('plan', type='hidden'),
                Field('skill', type='hidden'),
                Field('level', type='number', max=5, min=1)
            ),
            FormActions(
                Submit('save', 'Add', css_class='btn btn-success'),
            )
        )

    class Meta:
        """
        Form settings
        """
        model = PlannedSkill
        exclude = ['position',]