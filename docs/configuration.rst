Configuration
=============

settings.py (Please note that below settings is required as INSTALLED_APPS)::

    # Specify channels configuration as follows:

    ISSUE_TRACKER_CHANNELS_CONFIGURATION = {
    "DISCORD": {
        "backend": "issue_tracker.channels.backends.discord_backend.DiscordChannel",
        "credentials": {
            # Configuration for sending notifications to a Discord channel
            "WEBHOOK_URL": "discord webhook api",
            # Other Discord-specific credentials
        }
    },
    "TEAMS": {
        "backend": "issue_tracker.channels.backends.teams_backend.TeamsChannel",
        "credentials": {
            # Configuration for sending notifications to a Microsoft Teams channel
            # The required configuration options will be specified here.
        }
    },
     "EMAIL": {
        "backend": "issue_tracker.channels.backends.email_backend.EmailChannel",
        "credentials": {
            # Configuration for sending notification to a email channel
        }
    },
    "DB": {
        "backend": "issue_tracker.channels.backends.db_backend.DBChannel",
        "credentials": {
            # Configuration for sending notification to a database channel.
        }
    }
}

    INSTALLED_APPS = [
        ...
        # The following apps is required:
       issue_tracker,
    ]