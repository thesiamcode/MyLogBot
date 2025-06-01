
# Discord Server Logger Bot

A Discord bot that logs all server activity including messages, edits, and deletions to a designated logging channel. The bot includes a Flask web server for keep-alive functionality and keyword highlighting features.

## Features

- **Message Logging**: Logs all new messages with user details, timestamps, and attachments
- **Edit Tracking**: Monitors message edits and shows before/after content
- **Deletion Monitoring**: Captures deleted messages before they're lost
- **Keyword Highlighting**: Automatically highlights messages containing specified keywords
- **Attachment Support**: Downloads and re-uploads file attachments to the log channel
- **Keep-Alive Server**: Built-in Flask server to prevent the bot from sleeping on free hosting
- **Rich Embeds**: Beautiful Discord embeds with user avatars, timestamps, and jump links

## Setup

### Prerequisites

- Python 3.11+
- Discord Bot Token
- Discord Server with appropriate permissions

### Environment Variables

Set up the following environment variables in your Replit Secrets:

```
DISCORD_TOKEN=your_discord_bot_token_here
LOG_CHANNEL_ID=123456789012345678
SERVER_ID=123456789012345678
```

### Bot Permissions

Your Discord bot needs the following permissions:
- View Channels
- Send Messages
- Embed Links
- Attach Files
- Read Message History
- Use Slash Commands

### Installation

1. Clone this repository to Replit
2. Install dependencies (automatically handled by Replit)
3. Set up your environment variables in Replit Secrets
4. Invite the bot to your Discord server
5. Run the project

## Configuration

### Keyword Highlighting

Edit the `HIGHLIGHT_KEYWORDS` list in `main.py` to customize which words trigger special highlighting:

```python
HIGHLIGHT_KEYWORDS = ["urgent", "important", "alert", "help"]
```

### Server and Channel IDs

- `SERVER_ID`: The Discord server (guild) ID where the bot should operate
- `LOG_CHANNEL_ID`: The channel where all logs will be sent

## Commands

- `/status` - Check if the bot is online and responding

## File Structure

```
├── main.py           # Main bot code with event handlers
├── keep_alive.py     # Flask server for keep-alive functionality
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## How It Works

1. **Keep-Alive**: The Flask server runs on port 8080 to keep the bot active
2. **Event Monitoring**: The bot listens for message events (create, edit, delete)
3. **Logging**: Creates rich embeds with user information and sends to log channel
4. **Attachment Handling**: Downloads and re-uploads file attachments to preserve them
5. **Keyword Detection**: Scans messages for important keywords and highlights them

## Deployment

This bot is designed to run on Replit. Simply click the "Run" button to start the bot. The Flask server will keep it alive even on free Replit accounts.

For production deployment, use Replit's deployment feature to ensure 24/7 uptime.

## Security Notes

- Never share your bot token publicly
- Use Replit Secrets to store sensitive information
- Regularly rotate your bot token if compromised
- Ensure the bot only has necessary permissions

## Troubleshooting

### Bot Not Responding
- Check that your bot token is correct in Secrets
- Verify the bot has proper permissions in your Discord server
- Ensure the SERVER_ID matches your Discord server

### Missing Logs
- Confirm LOG_CHANNEL_ID is correct
- Check that the bot can send messages in the log channel
- Verify the bot has "Embed Links" and "Attach Files" permissions

### Attachment Issues
- Ensure the bot has "Attach Files" permission
- Check file size limits (Discord has an 8MB limit for free servers)

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
