from django.contrib import admin

from .models import Plan, PlannedSkill


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'character')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


class PlannedSkillAdmin(admin.ModelAdmin):
    list_display = ('plan','skill', 'level', 'position')
    list_filter = ()
    search_fields = ()
    date_hierarchy = ''


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlannedSkill, PlannedSkillAdmin)