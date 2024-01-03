from unittest import mock

import pytest
from django.core.exceptions import ImproperlyConfigured

from tracify import app_settings
from tracify.channels.channel import Channel


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
        Test case to verify the behavior of `process_exception` when tracify channels configuration is missing.

        It asserts that the method raises an ImproperlyConfigured exception.

        Args:
            error_notification_middleware: An instance of ErrorNotificationMiddleware.

        """
        # Mock the app_settings.TRACIFY_CHANNELS_CONFIGURATION to be empty
        with mock.patch(
            "tracify.middleware.app_settings.TRACIFY_CHANNELS_CONFIGURATION",
            {},
        ):
            # Define a sample request and exception
            request = mock.Mock()
            exception = Exception("Sample exception")

            with pytest.raises(ImproperlyConfigured) as excinfo:
                error_notification_middleware.process_exception(request, exception)
            # Assert that the exception was raised with the expected message
            assert str(excinfo.value) == "tracify channels configuration missing"

    def test_process_exception_valid_configuration(
        self, error_notification_middleware, tracify_channels_configuration
    ):
        """
        Test case to verify the behavior of `process_exception` with a valid tracify channels configuration.

        It checks if the send_notification method is called on the channel object.

        Args:
            error_notification_middleware: An instance of ErrorNotificationMiddleware.
            tracify_channels_configuration: Fixture providing a valid tracify channels configuration.

        """
        channel_mock = mock.Mock()
        channel_mock.send_notification = mock.Mock()
        error_notification_middleware.add_channel("channel_name", channel_mock)
        request = mock.Mock()
        exception = ValueError("Test Exception")
        app_settings.TRACIFY_CHANNELS_CONFIGURATION = {
            "channel_name": "configuration_data"
        }
        error_notification_middleware.process_exception(request, exception)

        channel_mock.send_notification.assert_called_once_with(
            configuration="configuration_data",
            request=request,
            exception_args=exception.args[0],
            data=mock.ANY,
            exception_type=exception.__class__.__name__,
        )
