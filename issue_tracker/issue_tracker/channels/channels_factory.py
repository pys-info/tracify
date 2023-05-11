from .backends.discord_backend import DiscordChannel
from .backends.teams_backend import TeamsChannel


class ChannelTransformer:
    """
       A class that maps channel names to channel objects for sending notifications.

       Attributes:
           channels (dict): A dictionary that maps channel names to channel objects.

       Methods:
           get_channel(name: str) -> Union[DiscordChannel, TeamsChannel]:
               Returns a channel object based on the given channel name.

       Example usage:
           channel_transformer = ChannelTransformer()
           channel = channel_transformer.get_channel('DISCORD')
           channel.send_notification(...)
       """

    def __init__(self):
        """
       Initializes a ChannelTransformer object with a dictionary of channel objects.
       """
        self.channels = {"DISCORD": DiscordChannel(name="DISCORD"), "TEAMS": TeamsChannel(name="TEAMS")}

    def get_channel(self, name: str):
        """
        Returns a channel object based on the given channel name.

        Args:
            name (str): The name of the channel.

        Returns:
            Union[DiscordChannel, TeamsChannel]: A channel object corresponding to the given name.

        Raises:
            ValueError: If an invalid channel name is provided.
        """
        channel = self.channels.get(name)
        if channel is not None:
            return channel
        else:
            raise ValueError(f"Invalid channel name: {name}")


# Create an instance of the ChannelTransformer class
channel_transformer = ChannelTransformer()
