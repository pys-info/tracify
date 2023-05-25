Different Channels Types
========

## 1) Discord:

A Discord communication channel is an online platform that facilitates real-time communication and collaboration between individuals or groups. It provides a space for users to engage in text-based chat, voice calls, and video conferences, fostering communication and building communities around shared interests. With features like voice channels, direct messaging, and file sharing, Discord channels offer a versatile and inclusive environment for socializing, organizing events, or coordinating teamwork. Whether for gaming, professional networking, or casual conversations, Discord communication channels serve as virtual meeting places, enabling users to connect, interact, and share experiences in a user-friendly and customizable setting.

##### **Configuring a webhook in Discord involves the following steps:**
1. Create a Discord server or choose an existing server where you have administrative privileges.
2. Select the channel in which you want to configure the webhook. Right-click on the channel and choose "Edit Channel" or "Channel Settings."
3. In the channel settings, navigate to the "Webhooks" tab. If you don't see this tab, ensure that you have the necessary permissions or switch to server settings if you are configuring a webhook for the entire server.
4. Click on the "Create Webhook" button or "New Webhook" option. A form will appear for webhook configuration.
5. Provide a name for the webhook. This can be the name of the bot or service that will be posting messages through the webhook.
6. Optionally, you can upload an image/avatar for the webhook to make it visually identifiable.
7. Copy the webhook URL. This URL will be used by the bot or service to send messages to the channel.

## 2) MS Teams:

Microsoft Teams is a collaborative communication and productivity platform that allows individuals and teams to work together seamlessly. It provides a centralized hub for chat, video meetings, file sharing, and project management, making it easy to collaborate and stay connected with colleagues and external partners. Teams offers a range of features including channels for organizing discussions, direct messaging for one-on-one conversations, and integrated file storage for easy access to shared documents. With its video conferencing capabilities, screen sharing, and collaboration tools like document editing, Teams empowers users to collaborate effectively, whether they are in the same office or working remotely. It integrates with other Microsoft services like Office 365, SharePoint, and OneDrive, providing a comprehensive and streamlined solution for communication, collaboration, and productivity within organizations of all sizes.

##### **Configuring a webhook in Teams involves the following steps:**

1) Open Microsoft Teams and navigate to the desired team or channel where you want to set up the webhook.
2) Click on the three-dot menu (ellipsis) next to the channel name and select "Connectors" from the dropdown menu.
3) In the Connectors window, search for "Incoming Webhook" or scroll down to find it. Click on the "Add" button next to it.
4) Provide a name for the webhook and, if desired, upload an image to represent the webhook.
5) Click on the "Create" button to create the webhook.
6) A unique URL will be generated for the webhook. Copy this URL as it will be used to send messages to the channel.

## 3) Email:

Email notifications allow you to deliver messages, updates, and important information to individuals or groups through their email addresses.

We have used the django backend email.

## 4) Database:

A channel that sends notifications by creating an Issue object in the database.

