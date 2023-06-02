from issue_tracker.channels.channel import Channel
from issue_tracker.models import Issue
import logging


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
            request = kwargs.get("request")
            Issue.objects.create(
                status_code="",
                description=kwargs.get("exception_args"),
                response=f"```{kwargs.get('data')}```",
                ip_address="ip_address",
                method=request.method,
                body=request.body,
                headers=request.headers,
                url=request.build_absolute_uri(),
                title=kwargs.get("exception_type"),
            )
        except Exception as err_info:
            logging.error(f"Database error while storing the issue: {err_info}")
