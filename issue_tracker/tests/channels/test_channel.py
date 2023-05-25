import pytest

from issue_tracker.channels.channel import Channel


class TestChannel:
    def test_channel_name(self):
        # Create a test channel
        channel_name = "test_channel"
        channel = Channel(name=channel_name)

        # Assert that the channel name is set correctly
        assert channel.name == channel_name

    def test_send_notification_not_implemented(self):
        # Create a test channel
        channel_name = "test_channel"
        channel = Channel(name=channel_name)

        # Assert that send_notification raises NotImplementedError
        with pytest.raises(NotImplementedError) as excinfo:
            channel.send_notification()
        # Assert that the exception was raised with the expected message
        assert (
            str(excinfo.value)
            == "send_notification method not implemented in the base class"
        )
