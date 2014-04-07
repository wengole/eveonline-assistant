from django.contrib import admin

from .models import ApiKey, Character, SkillTrained, AttributeValues


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('key_id', 'verification_code')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'enabled', 'apikey', 'user', 'name', 'skillpoints')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class SkillTrainedAdmin(admin.ModelAdmin):
    list_display = ('character', 'skill', 'skillpoints', 'level')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class AttributeValuesAdmin(admin.ModelAdmin):
    list_display = ('character', 'attribute', 'base', 'bonus')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


admin.site.register(ApiKey, ApiKeyAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(SkillTrained, SkillTrainedAdmin)
admin.site.register(AttributeValues, AttributeValuesAdmin)