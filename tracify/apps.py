from django.apps import AppConfig


class TracifyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracify"

    def ready(self):
        from tracify import signals
