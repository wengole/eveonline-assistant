from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, HTML, \
    Field, Div
from django import forms
from django.forms import ModelForm

from .models import ApiKey


class ApiKeyForm(ModelForm):
    """
    Simple form to add a new API Key
    """

    def __init__(self, *args, **kwargs):
        super(ApiKeyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                'Add new API Key',
                'key_id',
                'verification_code'
            ),
            FormActions(
                Submit('save', 'Add', css_class='btn btn-success'),
                Reset('reset', 'Reset', css_class='btn btn-default')
            )
        )

    class Meta:
        """
        Form settings
        """
        model = ApiKey
        exclude = ['user', ]


class CharacterForm(ModelForm):
    """
    Form to add character with a field to select API Key or add new
    """
    char_ids = forms.MultipleChoiceField()

    def __init__(self, user=None, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                'Add new character(s)',
                Field('apikey', placeholder='Select API Key'),
                'char_ids'
            ),
            FormActions(
                Submit('save', 'Add', css_class='btn btn-success'),
                Reset('reset', 'Reset', css_class='btn btn-default')
            )
        )
        if user.has_apikeys():
            self.fields['apikey'] = forms.ModelChoiceField(
                queryset=user.api_keys.all(),
                empty_label=''
            )
        else:
            self.helper['apikey'].update_attributes(
                placeholder='No API Keys'
            )
            self.helper.layout[0].insert(
                1,
                Div(
                    HTML('<a href="" class="btn btn-success">Add API Key</a>'),
                    css_class='form-group'
                )
            )

    class Meta:
        """
        Form settings
        """
        model = ApiKey
        exclude = ['user', ]