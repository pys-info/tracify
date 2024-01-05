import pytest

from tracify.channels.backends.discord import DiscordChannel
from tracify.channels.channels_factory import ChannelTransformer


@pytest.fixture
def tracify_channels_configuration():
    # Define the configuration dictionary
    configuration = {
        "CHANNEL_ONE": {
            "BACKEND": "fake channel class path",
            "WEBHOOK_URL": "fake channel one webhook url",
        },
        "CHANNEL_TWO": {
            "BACKEND": "fake channel class path",
            "WEBHOOK_URL": "fake channel two webhook url",
        },
    }
    return configuration


@pytest.fixture
def discord_channel():
    return DiscordChannel(name="dummy_channel")


@pytest.fixture
def channel_transformer():
    return ChannelTransformer()
