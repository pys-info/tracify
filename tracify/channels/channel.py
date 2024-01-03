class Channel:
    """
    Base class for tracify channels.
    """

    def __init__(self, name: str):
        """
        Initializes Channel object.

        Args:
            name (str): The name of the tracify channel.
        """
        self.name = name

    def send_notification(self, **kwargs):
        """
        Sends a notification to the tracify channel.

        Raises:
            NotImplementedError: If the send_notification method is not implemented in a subclass.
        """
        raise NotImplementedError(
            "send_notification method not implemented in the base class"
        )
