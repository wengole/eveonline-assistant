from django.contrib import admin

from .models import Group, Skill, Requirement, Attribute


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'published', 'group', 'name', 'rank', 'description', 'attribute', 'attribute')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class RequirementAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


admin.site.register(Group, GroupAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Attribute, AttributeAdmin)
