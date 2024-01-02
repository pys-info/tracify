from django.contrib import admin

from issue_tracker.db_backend.models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
