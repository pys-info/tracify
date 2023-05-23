from issue_tracker.channels.channel import Channel


class EmailChannel(Channel):
    def send_notification(self, **kwargs):
        pass
