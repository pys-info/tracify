import sys
import traceback
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .channels.backends.discord_backend import IssueTrackerChannel
from .channels.channels_factory import channel_transformer


class ExceptionHandleMiddleware:
    def __init__(self, get_response=None):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response
        self.channels = {}

    def __call__(self, request):
        return self.get_response(request)

    def add_channel(self, name: str, channel: IssueTrackerChannel):
        self.channels[name] = channel

    def process_exception(self, request, exception):
        exception_type = exception.__class__.__name__
        kind, info, data = sys.exc_info()
        data = "\n".join(traceback.format_exception(kind, info, data))

        if not settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION:
            raise ImproperlyConfigured("issue tracker channels configuration missing")

        for channel_name in settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION:
            channel = self.channels.get(channel_name)
            if not channel:
                # Create the channel object if not already created
                channel = channel_transformer.get_channel(name=channel_name)
                self.add_channel(channel_name, channel)
            channel.send_notification(
                configuration=settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION[channel_name], request=request,
                data=data, exception_type=exception_type
            )
