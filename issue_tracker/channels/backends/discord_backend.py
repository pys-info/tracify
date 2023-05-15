import json

from discord_webhook import DiscordWebhook, DiscordEmbed
from django.core.exceptions import ImproperlyConfigured


class Channel:
    """
    Base class for issue tracker channels.
    """
    def __init__(self, name: str):
        """
        Initializes Channel object.

        Args:
            name (str): The name of the issue tracker channel.
        """
        self.name = name

    def send_notification(self, **kwargs):
        """
        Sends a notification to the issue tracker channel.

        Raises:
            NotImplementedError: If the send_notification method is not implemented in a subclass.
        """
        raise NotImplementedError("send_notification method not implemented in the base class")


class DiscordChannel(Channel):
    """
    Sends notifications to a Discord channel.
    """
    def send_notification(self, **kwargs):
        """
        Sends a notification to a Discord channel.

        Args:
            **kwargs: Keyword arguments containing the notification data.

        Raises:
            ImproperlyConfigured: If the Discord Webhook URL is missing in the configuration.
        """
        _configuration = kwargs.get("configuration")
        if not _configuration.get("WEBHOOK_URL"):
            raise ImproperlyConfigured("Discord Webhook URL missing")

        webhook = DiscordWebhook(
            url=_configuration.get("WEBHOOK_URL"),
            content=kwargs.get("request").build_absolute_uri(),
            username="Issue Tracker",
        )
        data = f"```{kwargs.get('data')}```"
        embed = DiscordEmbed(title=kwargs.get("exception_type"), description=data, color="03b2f8")
        embed.add_embed_field(name="User", value=kwargs.get("request").user.username, inline=True)
        embed.add_embed_field(name="Method", value=kwargs.get("request").method, inline=True)
        embed.add_embed_field(name="GET", value=json.dumps(kwargs.get("request").GET), inline=False)
        embed.add_embed_field(name="POST", value=json.dumps(kwargs.get("request").POST), inline=False)
        embed.add_embed_field(name="File", value=json.dumps(kwargs.get("request").FILES), inline=False)
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
