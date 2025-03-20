from requests.exceptions import InvalidURL
from urllib3.exceptions import LocationParseError
from urllib3.util import parse_url

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


TRACIFY_CHANNELS_CONFIGURATION = settings.TRACIFY_CHANNELS_CONFIGURATION

if TRACIFY_CHANNELS_CONFIGURATION.get("EMAIL", False):
    if settings.EMAIL_ADMIN_USER and settings.EMAIL_HOST_USER:
        EMAIL_ADMIN_USER = settings.EMAIL_ADMIN_USER
        EMAIL_HOST_USER = settings.EMAIL_HOST_USER
    else:
        raise AttributeError(
            "EMAIL_ADMIN_USER / EMAIL_HOST_USER is not defined in settings.py"
        )


class TracifyConfigurationValidator:
    def __init__(self, channels_configuration):
        self.channels_configuration = channels_configuration

    def validate_channel_webhooks(self, channels):
        for channel in channels:
            config = self.channels_configuration.get(channel)

            if config:
                webhook_url = config.get("WEBHOOK_URL")
                if webhook_url:
                    try:
                        scheme, auth, host, port, path, query, fragment = parse_url(webhook_url)
                    except LocationParseError as e:
                        raise InvalidURL(*e.args)

                    if not scheme or not host:
                        raise ValueError(f"Invalid URL for {channel} webhook.")
                else:
                    red_color = "\033[91m"  # ANSI escape code for red text
                    reset_color = "\033[0m"  # Reset to default color
                    warnings.warn(
                        f"{red_color}⚠️  WARNING: The webhook URL for channel '{channel}' is missing in TRACIFY_CHANNELS_CONFIGURATION.{reset_color}",
                        UserWarning
                    )
                    # raise ImproperlyConfigured(f"WEBHOOK of {channel} is missing in TRACIFY_CHANNELS_CONFIGURATION")

    def validate_database(self):
        if "DB" in self.channels_configuration and "tracify.db_backend" not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured("Missing tracify.db_backend in INSTALLED_APPS")


# Usage
validator = TracifyConfigurationValidator(TRACIFY_CHANNELS_CONFIGURATION)

# Validate channel webhooks
validator.validate_channel_webhooks(["DISCORD", "TEAMS",  "SLACK"])

# Validate channel database
validator.validate_database()
