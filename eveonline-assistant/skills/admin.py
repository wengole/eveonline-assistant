from django import forms
from django.contrib import admin
from django_select2 import Select2MultipleWidget

from .models import Group, Skill, Requirement, Attribute


class SkillForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Skill
        widgets = {
            'required_skills': Select2MultipleWidget(
                select2_options={'multiple': True}
            )
        }


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SkillAdmin(admin.ModelAdmin):
    form = SkillForm
    list_display = (
        'id',
        'published',
        'group',
        'name',
        'rank',
        'description',
        'primary_attribute',
        'secondary_attribute'
    )


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level')


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Group, GroupAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Attribute, AttributeAdmin)
