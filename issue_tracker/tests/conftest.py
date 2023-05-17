import pytest


@pytest.fixture
def issue_tracker_channels_configuration():
    # Define the configuration dictionary
    configuration = {
        "CHANNEL_ONE": {
            "class": "fake channel class path",
            "credentials": {
                "WEBHOOK_URL": "fake channel one webhook url",
                # Other Discord-specific credentials
            }
        },
        "CHANNEL_TWO": {
            "class": "fake channel class path",
            "credentials": {
                "WEBHOOK_URL": "fake channel two webhook url",
                # Configuration for sending notifications to a Microsoft Teams channel
                # The required configuration options will be specified here.
            }
        },
    }
    return configuration
