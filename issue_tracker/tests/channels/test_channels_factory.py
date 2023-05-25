import pytest


class TestChannelTransformer:
    def test_get_channel_invalid_name(self, channel_transformer):
        # Mock the channel instance
        # Mock the channels dictionary
        with pytest.raises(ValueError) as exc:
            channel_transformer.get_channel("INVALID")

        # Assert that the correct exception is raised
        assert str(exc.value) == "Invalid channel name: INVALID"
