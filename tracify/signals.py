import sys
import traceback

from django.core.exceptions import ImproperlyConfigured
from django.core.signals import got_request_exception
from django.dispatch import receiver
from django.views.debug import ExceptionReporter

from tracify import app_settings
from tracify.channels.channels_factory import channel_transformer


@receiver(got_request_exception)
def exception_notifier(sender, request, **kwargs):
    """
    Process the exception and send notifications to the configured tracify channels.

    Args:
        sender :
        request: The request object.

    Raises:
        ImproperlyConfigured: If the tracify channels configuration is missing.
    """
    kind, info, data = sys.exc_info()

    exception = ExceptionReporter(request, kind, info, data).exc_value
    exception_args = exception.args[0] if len(exception.args) > 0 else ""
    exception_type = exception.__class__.__name__

    data = "\n".join(traceback.format_exception(kind, info, data))

    if not app_settings.TRACIFY_CHANNELS_CONFIGURATION:
        raise ImproperlyConfigured("tracify channels configuration missing")

    for channel_name in app_settings.TRACIFY_CHANNELS_CONFIGURATION:
        channel = channel_transformer.get_channel(name=channel_name)
        channel.send_notification(
            configuration=app_settings.TRACIFY_CHANNELS_CONFIGURATION[channel_name],
            request=request,
            exception_args=exception_args,
            data=data,
            exception_type=exception_type,
        )
