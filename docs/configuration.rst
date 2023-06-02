Configuration
=============

settings.py (Please note that below settings is required as INSTALLED_APPS)::

    # Specify channels configuration as follows:

    ISSUE_TRACKER_CHANNELS_CONFIGURATION = {
    "DISCORD": {
        "BACKEND": "issue_tracker.channels.backends.discord_backend.DiscordChannel",
        "WEBHOOK_URL": os.environ.get("WEBHOOK_URL"),
    },
    "TEAMS": {
        "BACKEND": "issue_tracker.channels.backends.teams_backend.TeamsChannel",
        "WEBHOOK_URL": os.environ.get("TEAMS_WEBHOOK_URL"),
    },
    "EMAIL": {
        "BACKEND": "issue_tracker.channels.backends.email_backend.EmailChannel",
    },
    "DB": {
        "BACKEND": "issue_tracker.channels.backends.db_backend.DBChannel",
    },
    "SLACk": {
        "BACKEND": "issue_tracker.channels.backends.slack_backend.SlackChannel",
        "WEBHOOK_URL": os.environ.get("SLACK_WEBHOOK_URL"),
    }
    ...
}

    INSTALLED_APPS = [
        ...
        # The following apps is required:
       issue_tracker,
    ]