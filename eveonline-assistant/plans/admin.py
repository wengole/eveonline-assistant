from django.contrib import admin

from .models import Plan, PlannedSkill


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'character')


class PlannedSkillAdmin(admin.ModelAdmin):
    list_display = ('plan','skill', 'level', 'position')


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlannedSkill, PlannedSkillAdmin)