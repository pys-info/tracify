import pytest
from django.core.exceptions import ImproperlyConfigured

from issue_tracker import app_settings


class TestIssueTrackerChannelsConfiguration:
    def test_missing_configuration(self, issue_tracker_channels_configuration):
        """
        Test case to verify that an ImproperlyConfigured exception is raised when the configuration is missing.
        """
        app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION = {}
        with pytest.raises(ImproperlyConfigured):
            raise ImproperlyConfigured(
                "ISSUE_TRACKER_CHANNELS_CONFIGURATION is missing"
            )

    def test_valid_configuration(self, issue_tracker_channels_configuration):
        """
        Test case to verify the validity of the configuration when it is present and valid.
        """
        app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION = (
            issue_tracker_channels_configuration
        )
        assert (
            app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION["CHANNEL_ONE"][
                "credentials"
            ]["WEBHOOK_URL"]
            == "fake channel one webhook url"
        )
        assert (
            app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION["CHANNEL_TWO"][
                "credentials"
            ]["WEBHOOK_URL"]
            == "fake channel two webhook url"
        )

    def test_invalid_configuration(self):
        """
        Test case to verify that an ImproperlyConfigured exception is raised when the configuration is invalid.
        """
        app_settings.ISSUE_TRACKER_CHANNELS_CONFIGURATION = "invalid_configuration"
        with pytest.raises(ImproperlyConfigured):
            raise ImproperlyConfigured(
                "ISSUE_TRACKER_CHANNELS_CONFIGURATION is invalid"
            )
