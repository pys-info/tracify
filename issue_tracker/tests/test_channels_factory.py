import pytest

from issue_tracker import app_settings
from issue_tracker.channels.channels_factory import ChannelTransformer


class TestChannelTransformer:
    def test_get_channel_invalid_name(self):
        # Mock the channel instance
        with pytest.raises(ValueError) as exc:
            ChannelTransformer().get_channel("INVALID")
        # Assert that the correct exception is raised
        assert str(exc.value) == "Invalid channel name: INVALID"
