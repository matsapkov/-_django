from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')

    actions = ['mark_completed']

    def mark_completed(self, request, queryset):
        queryset.update(status='Completed')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task')
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority')
        }),
    )

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task')
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority')
        }),
    )


# Register your models here.
