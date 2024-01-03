from django.conf import settings

TRACIFY_CHANNELS_CONFIGURATION = settings.TRACIFY_CHANNELS_CONFIGURATION

if settings.TRACIFY_CHANNELS_CONFIGURATION.get('EMAIL', False):
    if settings.EMAIL_ADMIN_USER and settings.EMAIL_HOST_USER:
        EMAIL_ADMIN_USER = settings.EMAIL_ADMIN_USER
        EMAIL_HOST_USER = settings.EMAIL_HOST_USER
    else:
        raise AttributeError(
            "EMAIL_ADMIN_USER / EMAIL_HOST_USER is not defined in settings.py"
        )
