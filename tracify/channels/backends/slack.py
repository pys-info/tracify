import json

from django.core.exceptions import ImproperlyConfigured
from slack_sdk.webhook import WebhookClient

from tracify.channels.channel import Channel
from tracify.utils import get_body_data


class SlackChannel(Channel):
    def send_notification(self, **kwargs):
        """
        Sends a notification to a Slack channel using a webhook.

        Args:
            **kwargs: Additional keyword arguments.
                - configuration (dict): Configuration parameters for the Slack channel.
                    - WEBHOOK_URL (str): The webhook URL for the Slack channel.

                - data (str): The notification data to send.

        Raises:
            ImproperlyConfigured: If the webhook URL is missing in the configuration.

        Returns:
            None
        """
        _configuration = kwargs.get("configuration")
        if not _configuration.get("WEBHOOK_URL"):
            raise ImproperlyConfigured("Slack Webhook URL missing")
        webhook = WebhookClient(
            _configuration.get("WEBHOOK_URL"),
        )

        message = {
            "text": kwargs.get("request").build_absolute_uri(),
            "attachments": [
                {
                    "title": kwargs.get("exception_type"),
                    "text": f"```{kwargs.get('data')}```",
                    "color": "#03b2f8",
                    "fields": [
                        {
                            "title": "Method",
                            "value": kwargs.get("request").method,
                            "short": True,
                        },
                        {
                            "title": "GET",
                            "value": json.dumps(kwargs.get("request").GET),
                            "short": False,
                        },
                        {
                            "title": "BODY",
                            "value": json.dumps(get_body_data(kwargs.get("request"))),
                            "short": False,
                        },
                    ],
                },
            ],
        }

        webhook.send(**message)
