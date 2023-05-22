import datetime
import json

import pymsteams
from django.core.exceptions import ImproperlyConfigured

from issue_tracker.channels.channel import Channel


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

        _configuration = kwargs.get("configuration")
        if not _configuration.get("WEBHOOK_URL"):
            raise ImproperlyConfigured("Teams Webhook URL missing")

        # Extract the 'data' value from kwargs and format it with triple backticks for code formatting
        data = f"```{kwargs.get('data')}```"

        # Create a connector card object with the Microsoft Webhook URL
        webhook = pymsteams.connectorcard(_configuration.get("WEBHOOK_URL"))
        webhook.color("03b2f8")  # Set the color of the card

        # Create Section 1
        Section1 = pymsteams.cardsection()
        Section1.title(kwargs.get("exception_type"))
        Section1.text(data)

        # Create Section 2
        Section2 = pymsteams.cardsection()
        request = kwargs.get("request")

        # Add facts to Section 2
        facts = {
            "USER": request.user.username if request.user.username else "None",
            "METHOD": request.method if request.method else "Method not found.",
            "GET": json.dumps(request.GET) if request.GET else "DATA not found.",
            "POST": json.dumps(request.POST) if request.POST else "DATA not found.",
            "FILES": json.dumps(request.FILES) if request.FILES else "DATA not found.",
            "TIMESTAMP": str(datetime.datetime.now())
        }
        for key, value in facts.items():
            Section2.addFact(key, value)

        # Add both Sections to the main card object
        webhook.addSection(Section1)
        webhook.addSection(Section2)

        webhook.summary("Issue Tracker")  # Set the summary of the card
        webhook.send()  # Send the message via the webhook
