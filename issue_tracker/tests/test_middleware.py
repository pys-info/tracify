from unittest import mock

import pytest
from django.core.exceptions import ImproperlyConfigured

from issue_tracker import app_settings
from issue_tracker.channels.channel import Channel


class TestErrorNotificationMiddleware:
    def test_add_channel(self, error_notification_middleware):
        """
        Test case to verify the `add_channel` method of ErrorNotificationMiddleware.

        It checks if a channel is successfully added to the middleware.

        Args:
            error_notification_middleware: An instance of ErrorNotificationMiddleware.

        """
        # Create a test channel and add it to the middleware
        channel_name = "test_channel"
        channel = Channel(name=channel_name)
        error_notification_middleware.add_channel(channel_name, channel)

        # Assert that the channel is added successfully
        assert channel_name in error_notification_middleware.channels
        assert error_notification_middleware.channels[channel_name] == channel

    def test_process_exception_missing_configuration(
        self, error_notification_middleware
    ):
        """
        Test case to verify the behavior of `process_exception` when issue tracker channels configuration is missing.

        It asserts that the method raises an ImproperlyConfigured exception.

        Args:
            error_notification_middleware: An instance of ErrorNotificationMiddleware.

        """
        # Mock the app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION to be empty
        with mock.patch(
            "issue_tracker.middleware.app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION",
            {},
        ):
            # Define a sample request and exception
            request = mock.Mock()
            exception = Exception("Sample exception")

            with pytest.raises(ImproperlyConfigured) as excinfo:
                error_notification_middleware.process_exception(request, exception)
            # Assert that the exception was raised with the expected message
            assert str(excinfo.value) == "issue tracker channels configuration missing"

    def test_process_exception_valid_configuration(
        self, error_notification_middleware, issue_tracker_channels_configuration
    ):
        """
        Test case to verify the behavior of `process_exception` with a valid issue tracker channels configuration.

        It checks if the send_notification method is called on the channel object.

        Args:
            error_notification_middleware: An instance of ErrorNotificationMiddleware.
            issue_tracker_channels_configuration: Fixture providing a valid issue tracker channels configuration.

        """
        # Set up a valid configuration
        app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION = {
            "CHANNEL_ONE": {
                "class": "fake channel class path",
                "credentials": {
                    "WEBHOOK_URL": "fake channel one webhook url",
                    # Other Discord-specific credentials
                },
            },
        }

        # Define a sample request and exception
        request = mock.Mock()
        exception = Exception("Sample exception")

        # Mock the channel object
        channel_mock = mock.Mock()
        error_notification_middleware.add_channel("CHANNEL_ONE", channel_mock)

        # Call the process_exception method
        error_notification_middleware.process_exception(request, exception)

        # Assert that the send_notification method is called on the channel object
        channel_mock.send_notification.assert_called_once_with(
            configuration=app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION[
                "CHANNEL_ONE"
            ]["credentials"],
            request=request,
            data=mock.ANY,
            exception_type=exception.__class__.__name__,
        )
