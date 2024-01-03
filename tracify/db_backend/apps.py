from django.apps import AppConfig


class DbBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracify.db_backend'
    verbose_name = "Tracify DB Backend"
