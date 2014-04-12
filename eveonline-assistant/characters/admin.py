from django.contrib import admin

from .models import ApiKey, Character, SkillTrained, AttributeValues


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key_id', 'verification_code')


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'enabled', 'apikey', 'user', 'name', 'skillpoints')


class SkillTrainedAdmin(admin.ModelAdmin):
    list_display = ('character', 'skill', 'skillpoints', 'level')


class AttributeValuesAdmin(admin.ModelAdmin):
    list_display = ('character', 'attribute', 'base', 'bonus')


admin.site.register(ApiKey, ApiKeyAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(SkillTrained, SkillTrainedAdmin)
admin.site.register(AttributeValues, AttributeValuesAdmin)