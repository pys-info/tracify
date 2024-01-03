import json
from datetime import datetime

from tracify.channels.channel import Channel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from tracify import app_settings
from tracify.utils import get_body_data


class EmailChannel(Channel):
    def send_notification(self, **kwargs):
        """
        Sends a notification email containing error details.

        Args:
            request (HttpRequest): The request object associated with the error.
            data (Any): The error data to be included in the email.

        Raises:
            EmailSendingError: If an error occurs while sending the email.

        Returns:
            None
        """
        request = kwargs.get("request")
        body = get_body_data(request)
        context = {
            "exception_type": kwargs.get("exception_type"),
            "error_tracback": str(kwargs.get("data")),
            "user": request.user if request.user.is_authenticated else None,
            "method": request.method,
            "url": request.build_absolute_uri(),
            "get": json.dumps(request.GET) if request.GET else "DATA not found.",
            "body": json.dumps(body) if body else "DATA not found.",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        html_content = render_to_string(template_name="issue_notifier.html", context=context)
        msg = EmailMultiAlternatives(from_email=app_settings.EMAIL_ADMIN_USER, subject="ERROR LOG",
                                     to=[app_settings.EMAIL_HOST_USER])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
