from .discord_backend import Channel


class TeamsChannel(Channel):
    """
    Sends notifications to a Microsoft Teams channel.
    """
    def send_notification(self, **kwargs):
        """Send a notification to Microsoft Teams.

        This method should be implemented to include the logic for sending a notification to a Microsoft Teams channel.

        Args:
            **kwargs: A dictionary of keyword arguments containing the information required for sending the notification
        """
