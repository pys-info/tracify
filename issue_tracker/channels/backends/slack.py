from django.core.exceptions import ImproperlyConfigured

from issue_tracker.channels.channel import Channel
from slack_sdk.webhook import WebhookClient


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
        webhook = WebhookClient(_configuration.get("WEBHOOK_URL"), )
        data = f"```{kwargs.get('data')}```"
        webhook.send(
            text="fallback",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": data
                    }
                }
            ]
        )

