from django.contrib import admin

from .models import Group, Skill, Attribute


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class SkillAdmin(admin.ModelAdmin):
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
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
    )
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


admin.site.register(Group, GroupAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Attribute, AttributeAdmin)
