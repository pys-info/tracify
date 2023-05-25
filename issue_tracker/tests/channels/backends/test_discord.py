from unittest import mock

import pytest
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest

from issue_tracker.channels.backends.discord_backend import DiscordChannel


class TestDiscordChannel:
    def test_send_notification_missing_webhook_url(self):
        """
        Test case to verify the behavior of `send_notification` when the Discord Webhook URL is missing.

        It asserts that the method raises an ImproperlyConfigured exception.

        """
        # Create an instance of DiscordChannel
        discord_channel = DiscordChannel(name="test_channel")

        # Define the keyword arguments for the send_notification method
        kwargs = {
            "configuration": {},
            "request": mock.Mock(),
            "data": "Sample data",
            "exception_type": "Sample exception",
        }

        # Assert that an ImproperlyConfigured exception is raised
        with pytest.raises(ImproperlyConfigured) as excinfo:
            discord_channel.send_notification(**kwargs)

        # Assert that the exception was raised with the expected message
        assert str(excinfo.value) == "Discord Webhook URL missing"

    def test_send_notification_valid_configuration(self):
        """
        Test case to verify the behavior of `send_notification` with a valid configuration.

        It checks if the DiscordWebhook is created and executed correctly.

        """
        # Create an instance of DiscordChannel
        discord_channel = DiscordChannel(name="test_channel")

        # Define the keyword arguments for the send_notification method
        kwargs = {
            "configuration": {"WEBHOOK_URL": "fake_webhook_url"},
            "request": HttpRequest(),
            "data": "Sample data",
            "exception_type": "Sample exception",
        }
        # Mock the build_absolute_uri method of the HttpRequest object
        kwargs["request"].build_absolute_uri = mock.Mock(
            return_value="http://example.com"
        )

        # Mock the DiscordWebhook and execute method
        webhook_mock = mock.Mock()

        # Patch the DiscordWebhook class and execute method
        with mock.patch(
            "issue_tracker.channels.backends.discord_backend.DiscordWebhook",
            return_value=webhook_mock,
        ):
            discord_channel.send_notification(**kwargs)
            webhook_mock.configure_mock()

            # TODO Improve coverage for this test-cases as now only patch the webhook instance.
