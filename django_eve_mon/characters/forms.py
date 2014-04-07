from crispy_forms.bootstrap import FormActions, FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Reset, HTML, \
    Field, Div, Button
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

    def __init__(self, user=None, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.fields['char_ids'] = forms.MultipleChoiceField()
        self.fields['apikey'] = forms.ModelChoiceField(
            queryset=user.api_keys.all(),
            empty_label=''
        )

        self.helper.layout = Layout(
            Fieldset(
                'Add new character(s)',
                Field('apikey', placeholder='Select API Key'),
                Field('char_ids', placeholder='Select characters')
            ),
            FormActions(
                Button(
                    'add-char',
                    'Add characters',
                    css_class='btn btn-success',
                ),
                HTML(
                    '<a href="{% url "characters:add_api" %}"'
                    ' class="btn btn-info">Add API Key</a>',
                ),
                Reset('reset', 'Reset', css_class='btn btn-warning'),
            )
        )
        if user.has_apikeys():
            pass
        else:
            self.helper['apikey'].update_attributes(
                placeholder='No API Keys',
                disabled='disabled'
            )
            self.helper['char_ids'].update_attributes(
                placeholder='Add an API Key',
                disabled='disabled'
            )
            self.helper.layout[1][0] = Button(
                'add-char',
                'Add characters',
                css_class='btn btn-success',
                disabled='disabled'
            )


    class Meta:
        """
        Form settings
        """
        model = ApiKey
        exclude = ['user', ]