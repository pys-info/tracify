import json
import logging

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from tracify.channels.channel import Channel
from tracify.db_backend.models import Issue
from tracify.utils import get_body_data


class DBChannel(Channel):
    """
    A channel that sends notifications by creating an Issue object in the database.
    """

    def send_notification(self, **kwargs):
        """
        Sends a notification by creating an Issue object in the database.

        Args:
            **kwargs: Keyword arguments containing the information required to create the Issue.
                - request (object): The request object associated with the issue.
                - exception_args (str): The description of the exception.
                - data (str): The response data.
                - exception_type (str): The type of the exception.
        """

        if "tracify.db_backend" not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured("Missing tracify.db_backend in INSTALLED_APPS")

        self.create_issue(**kwargs)

    @staticmethod
    def create_issue(**kwargs):
        """
        Creates an Issue object in the database.

        Args:
            **kwargs: Keyword arguments containing the information required to create the Issue.
                - request (object): The request object associated with the issue.
                - exception_args (str): The description of the exception.
                - data (str): The response data.
                - exception_type (str): The type of the exception.
        """
        try:
            body = get_body_data(kwargs.get("request"))
            additional_data = {
                "response": kwargs.get("data"),
                "method": kwargs.get("request").method,
                "headers": dict(kwargs.get("request").headers),
                "body": body,
                "get": json.dumps(kwargs.get("request").GET),
                "url": kwargs.get("request").build_absolute_uri(),
            }

            Issue.objects.create(
                data=additional_data,
                description=kwargs.get("exception_args"),
                title=kwargs.get("exception_type"),
            )
        except Exception as err_info:
            logging.error(f"Database error while storing the issue: {err_info}")
