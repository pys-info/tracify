
<h1><i> django-issue-tracker</i></h1>

**[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)**
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>

## Project description
Django Issue Tracker is a robust package designed to streamline issue tracking within Django web applications.The package supports various notification channels, allowing teams to receive updates through their preferred communication methods.By integrating this package, teams can collaborate seamlessly, expedite issue resolution, and enhance overall efficiency throughout the software development and maintenance lifecycle in Django projects.
## Feature

* **Multiple Notification Channels:**
Django Issue Tracker supports multiple channels for sending notifications, such as email, MS Teams, Discord, or any other custom channels. This flexibility allows teams to choose the most effective means of receiving notifications based on their communication preferences and workflows.
* **Real-Time Error Monitoring:**
Get instant notifications and detailed stack traces for errors occurring in your application, allowing you to respond quickly.

## Requirements
- Python 3.5, 3.6, 3.7, 3.8, 3.9, or 3.10
- Django (3.0+)
## Supported Channels
- Discord
- MS Teams
- Email
- Database
- Slack

## Installation 

**Python package:**

    pip install pys-django-issue-tracker

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
    # If you are using EMAIL in above configuration you must need to configure EMAIL Configuration with EMAIL_ADMIN_USER and EMAIL_HOST_USER in settings.py
    "DB": {
        "BACKEND": "issue_tracker.channels.backends.db.DBChannel",
    },
    "SLACK": {
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

    MIDDLEWARE = [
        ...
        # The following middleware is required:
        'issue_tracker.middleware.ErrorNotificationMiddleware'
    ]
## Acknowledgements
 - We would like to express our gratitude to the following individuals and organizations for their contributions, support, and inspiration:
   - PySquad Informatics LLP(https://pysquad.com/)

 - We also want to extend our thanks to the open-source community for their continuous efforts and contributions to the Python ecosystem. We greatly appreciate the work of all the developers, contributors, and maintainers of the libraries and frameworks that this package relies on.
 - Finally, we would like to thank our users for their feedback, bug reports, and feature requests. Your input has been invaluable in shaping the evolution of this package.
 - We are grateful to everyone who has played a part in making this package what it is today, and we look forward to continued collaboration and improvement in the future.

## Configuration
-  The package can be configured using configuration file or enviroment variable.Refer to the configuration documentation for details information on available setting and customization options.See details information inside `docs/configuration.rst`.
-  Troubleshooting and Support If you encounter any issues or have questions, please visit our support page or check out the FAQs for common troubleshooting steps and answers to frequently asked questions. See details information inside `docs/faq.rst`.
-  Changelog to see the full history of changes made to the package.please refer to the changlog.See details information inside `ChangLog.rst`.
-  This packages is licenced under the MIT Licence.See details information inside`License`.
-  Refer to the Channels documentation for details information on available channels.See details information inside `docs/channels.rst`
-  Release version related information you can get inside the release-notes documents.See details information inside `docs/release-notes.rst`

## License
*MIT License:* <https://choosealicense.com/licenses/mit/>

## Contact
For any inquiries or feedback, you can reach us at xyz@example.com or join our community channel.
