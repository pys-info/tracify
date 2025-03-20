
<h1><i> tracify </i></h1>

**[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)**
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>

## Project description
Django Tracify is a robust package designed to streamline issue tracking within Django web applications.The package supports various notification channels, allowing teams to receive updates through their preferred communication methods.By integrating this package, teams can collaborate seamlessly, expedite issue resolution, and enhance overall efficiency throughout the software development and maintenance lifecycle in Django projects.
## Feature

* **Multiple Notification Channels:**
Django Tracify supports multiple channels for sending notifications, such as email, MS Teams, Discord, or any other custom channels. This flexibility allows teams to choose the most effective means of receiving notifications based on their communication preferences and workflows.
* **Real-Time Error Monitoring:**
Get instant notifications and detailed stack traces for errors occurring in your application, allowing you to respond quickly.

## Requirements
- Python >=3.8
- Django >=3.1
## Supported Channels
- Discord
- MS Teams
- Email
- Database
- Slack

## Installation

**Python package:**

    pip install tracify

settings.py (Please note that below settings is required as INSTALLED_APPS)::
    INSTALLED_APPS = [
        ...
        # The following apps is required:
       "tracify",
    ]

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
    # If you are using EMAIL in above configuration you must need to configure EMAIL Configuration with EMAIL_ADMIN_USER and EMAIL_HOST_USER in settings.py
    "DB": {
        "BACKEND": "tracify.channels.backends.db.DBChannel",
    },
    # If you are using DB in above configuration you must need to add tracify.db_backend in INSTALLED_APP
    "SLACK": {
        "BACKEND": "tracify.channels.backends.slack.SlackChannel",
        "WEBHOOK_URL": <"SLACK_WEBHOOK_URL">,
    }
    ...
}

    

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
For any inquiries or feedback, you can reach us at contact@pysquad.com or join our community channel from here https://discord.gg/d2yxwBCd.
