import importlib

from issue_tracker import app_settings


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
        Configures the issue tracker channels based on the provided app settings.

        The method iterates over the `ISSUE_TRACKER_CHANNELS_CONFIGURATION` dictionary in the `app_settings` module,
        which contains the configuration for each channel. It dynamically imports the channel class, creates an instance
        of the class, and sets the credentials for the channel.

        Args:
            None.

        Returns:
            None.

        Raises:
            ImportError: If there is an error while importing the channel class.
            AttributeError: If the channel class or its attributes are not found.

        """
        self.channels = {}
        for (
            channel_name,
            channel_config,
        ) in app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION.items():

            # Extract channel class and credentials from configuration
            channel_class_path = (
                channel_config["class"],
                channel_config["credentials"],
            )

            # Dynamically import the channel class
            module_name, class_name = channel_class_path[0].rsplit(".", 1)
            channel_module = importlib.import_module(module_name)
            ChannelClass = getattr(channel_module, class_name)

            # Create an instance of the channel class and set the credentials configuration
            channel_instance = ChannelClass(name=channel_name)

            # Add the channel instance to the channels dictionary
            self.channels[channel_name] = channel_instance

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
