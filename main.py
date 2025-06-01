# 🌟 Discord Server Cloner + Logger Bot (Final with Categories & Voice Channels)
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# Start Flask server for Replit keep-alive
keep_alive()

# Setup bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Get secrets from Replit
TOKEN = os.getenv("DISCORD_TOKEN")
SOURCE_SERVER_ID = int(os.getenv("SOURCE_SERVER_ID"))
LOGGING_SERVER_ID = int(os.getenv("LOGGING_SERVER_ID"))

# === Helpers ===
def get_category_by_name(guild, name):
    return discord.utils.get(guild.categories, name=name)

def get_channel_by_name(guild, name):
    return discord.utils.get(guild.channels, name=name)

async def clone_server_structure():
    source_guild = bot.get_guild(SOURCE_SERVER_ID)
    logging_guild = bot.get_guild(LOGGING_SERVER_ID)

    if not source_guild or not logging_guild:
        print("❌ Could not find source or logging server.")
        return

    # Clone categories and channels
    for category in source_guild.categories:
        log_category = get_category_by_name(logging_guild, category.name)
        if not log_category:
            log_category = await logging_guild.create_category(category.name)
            print(f"✅ Created category: {category.name}")

        for channel in category.channels:
            if isinstance(channel, discord.TextChannel):
                if not get_channel_by_name(logging_guild, channel.name):
                    await logging_guild.create_text_channel(name=channel.name, category=log_category)
                    print(f"✅ Created text channel: {channel.name} in {category.name}")
            elif isinstance(channel, discord.VoiceChannel):
                if not get_channel_by_name(logging_guild, channel.name):
                    await logging_guild.create_voice_channel(name=channel.name, category=log_category)
                    print(f"✅ Created voice channel: {channel.name} in {category.name}")

    # Clone uncategorized channels
    for channel in source_guild.channels:
        if isinstance(channel, discord.TextChannel) and channel.category is None:
            if not get_channel_by_name(logging_guild, channel.name):
                await logging_guild.create_text_channel(name=channel.name)
                print(f"✅ Created uncategorized text channel: {channel.name}")
        elif isinstance(channel, discord.VoiceChannel) and channel.category is None:
            if not get_channel_by_name(logging_guild, channel.name):
                await logging_guild.create_voice_channel(name=channel.name)
                print(f"✅ Created uncategorized voice channel: {channel.name}")

# Ensure a channel exists in logging server (for text logging)
async def ensure_logging_channel_exists(channel_name):
    logging_guild = bot.get_guild(LOGGING_SERVER_ID)
    return get_channel_by_name(logging_guild, channel_name) or await logging_guild.create_text_channel(name=channel_name)

# === Events ===
@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    await clone_server_structure()
    print("✅ Server structure cloned successfully!")

@bot.event
async def on_guild_channel_create(channel):
    if channel.guild.id != SOURCE_SERVER_ID:
        return
    logging_guild = bot.get_guild(LOGGING_SERVER_ID)
    log_category = None
    if channel.category:
        log_category = get_category_by_name(logging_guild, channel.category.name)
        if not log_category:
            log_category = await logging_guild.create_category(channel.category.name)
    if isinstance(channel, discord.TextChannel):
        await logging_guild.create_text_channel(channel.name, category=log_category)
        print(f"✅ Synced new text channel: {channel.name}")
    elif isinstance(channel, discord.VoiceChannel):
        await logging_guild.create_voice_channel(channel.name, category=log_category)
        print(f"✅ Synced new voice channel: {channel.name}")

@bot.event
async def on_guild_channel_update(before, after):
    if before.guild.id != SOURCE_SERVER_ID:
        return
    logging_guild = bot.get_guild(LOGGING_SERVER_ID)
    log_channel = get_channel_by_name(logging_guild, before.name)
    if log_channel:
        await log_channel.edit(name=after.name)
        print(f"✏️ Renamed '{before.name}' to '{after.name}'")

# === Message Logging ===
@bot.event
async def on_message(message):
    if message.author.bot or message.guild.id != SOURCE_SERVER_ID:
        return
    log_channel = get_channel_by_name(bot.get_guild(LOGGING_SERVER_ID), message.channel.name)
    if log_channel and isinstance(log_channel, discord.TextChannel):
        await log_message(message, "New Message")
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    if after.author.bot or after.guild.id != SOURCE_SERVER_ID:
        return
    log_channel = get_channel_by_name(bot.get_guild(LOGGING_SERVER_ID), after.channel.name)
    if log_channel and isinstance(log_channel, discord.TextChannel):
        await log_message(after, "Edited Message", old_content=before.content)

@bot.event
async def on_message_delete(message):
    if message.author.bot or message.guild.id != SOURCE_SERVER_ID:
        return
    log_channel = get_channel_by_name(bot.get_guild(LOGGING_SERVER_ID), message.channel.name)
    if log_channel and isinstance(log_channel, discord.TextChannel):
        await log_message(message, "Deleted Message")

async def log_message(message, log_type, old_content=None):
    log_channel = get_channel_by_name(bot.get_guild(LOGGING_SERVER_ID), message.channel.name)
    if not log_channel:
        return

    embed = discord.Embed(
        title=log_type,
        description=message.content or "*No text*",
        color=discord.Color.green() if log_type == "New Message" else discord.Color.orange() if log_type == "Edited Message" else discord.Color.red(),
        timestamp=message.created_at
    )
    embed.set_author(
        name=str(message.author),
        icon_url=message.author.avatar.url if message.author.avatar else None
    )
    embed.add_field(name="Message Link", value=message.jump_url, inline=False)
    if old_content and log_type == "Edited Message":
        embed.add_field(name="Old Content", value=old_content, inline=False)
    embed.set_footer(text=f"User ID: {message.author.id}")
    files = [await a.to_file() for a in message.attachments]
    await log_channel.send(embed=embed, files=files)

# /status command (only in logging server)
@bot.command()
async def status(ctx):
    if ctx.guild.id != LOGGING_SERVER_ID:
        return
    await ctx.send("✅ I'm online!")

# Start the bot
bot.run(TOKEN)
