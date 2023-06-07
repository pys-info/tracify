Configuration
=============

settings.py (Please note that below settings is required as INSTALLED_APPS)::

    # Specify channels configuration as follows:

    ISSUE_TRACKER_CHANNELS_CONFIGURATION = {
    "DISCORD": {
        "BACKEND": "issue_tracker.channels.backends.discord.DiscordChannel",
        "WEBHOOK_URL": <"DISCORD_WEBHOOK_URL">,
    },
    "TEAMS": {
        "BACKEND": "issue_tracker.channels.backends.teams.TeamsChannel",
        "WEBHOOK_URL": <"TEAMS_WEBHOOK_URL">,
    },
    "EMAIL": {
        "BACKEND": "issue_tracker.channels.backends.email.EmailChannel",
    },
    "DB": {
        "BACKEND": "issue_tracker.channels.backends.db.DBChannel",
    },
    "SLACk": {
        "BACKEND": "issue_tracker.channels.backends.slack.SlackChannel",
        "WEBHOOK_URL": <"SLACK_WEBHOOK_URL">,
    }
    ...
}

    INSTALLED_APPS = [
        ...
        # The following apps is required:
       issue_tracker,
    ]