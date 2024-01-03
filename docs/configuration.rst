Configuration
=============

settings.py (Please note that below settings is required as INSTALLED_APPS)::

    # Specify channels configuration as follows:

    TRACIFY_CHANNELS_CONFIGURATION = {
    "DISCORD": {
        "BACKEND": "tracify.channels.backends.discord.DiscordChannel",
        "WEBHOOK_URL": <"DISCORD_WEBHOOK_URL">,
    },
    "TEAMS": {
        "BACKEND": "tracify.channels.backends.teams.TeamsChannel",
        "WEBHOOK_URL": <"TEAMS_WEBHOOK_URL">,
    },
    "EMAIL": {
        "BACKEND": "tracify.channels.backends.email.EmailChannel",
    },
    "DB": {
        "BACKEND": "tracify.channels.backends.db.DBChannel",
    },
    "SLACk": {
        "BACKEND": "tracify.channels.backends.slack.SlackChannel",
        "WEBHOOK_URL": <"SLACK_WEBHOOK_URL">,
    }
    ...
}

    INSTALLED_APPS = [
        ...
        # The following apps is required:
       tracify,
    ]