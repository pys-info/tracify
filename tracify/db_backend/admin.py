from django.contrib import admin

from tracify.db_backend.models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
