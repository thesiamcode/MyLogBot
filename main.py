import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# Start the Flask server
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))
SERVER_ID = int(os.getenv("SERVER_ID"))

HIGHLIGHT_KEYWORDS = ["urgent", "important"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Helper: Create an embed with user details
def create_embed(title, message, content):
    embed = discord.Embed(title=title, description=content or "*No text content*", color=discord.Color.blue())
    embed.set_author(name=f"{message.author} ({message.author.id})", icon_url=message.author.avatar.url if message.author.avatar else None)
    embed.timestamp = message.created_at
    embed.url = message.jump_url  # Link to the original message
    embed.add_field(name="Channel", value=message.channel.mention, inline=False)
    return embed

# Helper: Get list of file attachments (if any)
async def get_attachments(message):
    files = []
    for attachment in message.attachments:
        try:
            file = await attachment.to_file()
            files.append(file)
        except Exception as e:
            print(f"Error downloading attachment: {e}")
    return files

# Log new messages
@bot.event
async def on_message(message):
    if message.author.bot or message.guild is None or message.guild.id != SERVER_ID:
        return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        return

    # Create embed for the message
    embed = create_embed("New Message", message, message.content)

    # Get attachments as files
    files = await get_attachments(message)

    await log_channel.send(embed=embed, files=files)

    # Highlight keywords (optional)
    if any(keyword.lower() in message.content.lower() for keyword in HIGHLIGHT_KEYWORDS):
        keyword_embed = create_embed("Keyword Detected!", message, message.content)
        await log_channel.send(embed=keyword_embed)

    await bot.process_commands(message)

# Log edited messages
@bot.event
async def on_message_edit(before, after):
    if before.author.bot or before.guild is None or before.guild.id != SERVER_ID:
        return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        return

    content = f"**Before:** {before.content or '*No text*'}\n\n**After:** {after.content or '*No text*'}"
    embed = create_embed("Edited Message", after, content)

    # Get attachments from the edited message (after)
    files = await get_attachments(after)

    await log_channel.send(embed=embed, files=files)

# Log deleted messages
@bot.event
async def on_message_delete(message):
    if message.author.bot or message.guild is None or message.guild.id != SERVER_ID:
        return

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        return

    embed = create_embed("Deleted Message", message, message.content)

    # Get attachments from the deleted message
    files = await get_attachments(message)

    await log_channel.send(embed=embed, files=files)

# /status command
@bot.command()
async def status(ctx):
    await ctx.send("I’m online!")

# Error handling
@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in {event}: {args} {kwargs}")

bot.run(TOKEN)
