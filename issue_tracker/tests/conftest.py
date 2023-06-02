import pytest

from issue_tracker.channels.backends.discord import DiscordChannel
from issue_tracker.channels.channels_factory import ChannelTransformer
from issue_tracker.middleware import ErrorNotificationMiddleware


@pytest.fixture
def issue_tracker_channels_configuration():
    # Define the configuration dictionary
    configuration = {
        "CHANNEL_ONE": {
            "class": "fake channel class path",
            "credentials": {
                "WEBHOOK_URL": "fake channel one webhook url",
                # Other Discord-specific credentials
            },
        },
        "CHANNEL_TWO": {
            "class": "fake channel class path",
            "credentials": {
                "WEBHOOK_URL": "fake channel two webhook url",
                # Configuration for sending notifications to a Microsoft Teams channel
                # The required configuration options will be specified here.
            },
        },
    }
    return configuration


@pytest.fixture
def error_notification_middleware():
    # Instance of ErrorNotificationMiddleware for testing
    return ErrorNotificationMiddleware()


@pytest.fixture
def discord_channel():
    return DiscordChannel(name="dummy_channel")


@pytest.fixture
def channel_transformer():
    return ChannelTransformer()
