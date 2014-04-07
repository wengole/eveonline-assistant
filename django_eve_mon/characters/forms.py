from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field, Button
from django import forms
from django.forms import ModelForm
from evelink.api import APIError

from .models import ApiKey


class ApiKeyForm(ModelForm):
    """
    Simple form to add a new API Key
    """

    def __init__(self, user, *args, **kwargs):
        super(ApiKeyForm, self).__init__(*args, **kwargs)
        self.user = user
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
            )
        )

    def clean(self):
        cleaned_data = super(ApiKeyForm, self).clean()
        apikey = ApiKey(
            key_id=cleaned_data.get('key_id'),
            verification_code=cleaned_data.get('verification_code'),
            user=self.user
        )
        try:
            apikey.get_characters()
        except APIError as e:
            raise forms.ValidationError(
                '%s' % e.message,
                'api-error'
            )
        return cleaned_data

    class Meta:
        """
        Form settings
        """
        model = ApiKey
        exclude = ['user', ]


class CharacterForm(forms.Form):
    """
    Form to add character with a field to select API Key or add new
    """

    def __init__(self, user=None, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.fields['char_ids'] = forms.ModelMultipleChoiceField(
            queryset=user.characters.filter(enabled=False),
            label='Characters'
        )
        self.fields['char_ids'].help_text = ''

        self.helper.layout = Layout(
            Fieldset(
                'Add new character(s)',
                Field('char_ids', placeholder='Select characters')
            ),
            FormActions(
                Button(
                    'add-char',
                    'Add characters',
                    css_class='btn btn-success',
                ),
                Button(
                    'add-api',
                    'Add API Key',
                    css_class='btn btn-info'
                ),
            )
        )
        if not user.has_disabled_characters():
            self.helper['char_ids'].update_attributes(
                placeholder='No disabled characters found. Add an API Key',
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