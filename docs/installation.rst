Installation
============

Python package::

    pip install django-issue-tracker

settings.py (Please note that below settings is required as INSTALLED_APPS)::

    # Specify channels configuration as follows:

    ISSUE_TRACKER_CHANNELS_CONFIGURATION = {
    "DISCORD": {
        "class": "issue_tracker.channels.backends.discord_backend.DiscordChannel",
        "credentials": {
            # Configuration for sending notifications to a Discord channel
            "WEBHOOK_URL": "discord webhook api",
            # Other Discord-specific credentials
        }
    },
    "TEAMS": {
        "class": "issue_tracker.channels.backends.teams_backend.TeamsChannel",
        "credentials": {
            # Configuration for sending notifications to a Microsoft Teams channel
            # The required configuration options will be specified here.
        }
    },
    ...
}

    INSTALLED_APPS = [
        ...
        # The following apps is required:
       issue_tracker,
    ]