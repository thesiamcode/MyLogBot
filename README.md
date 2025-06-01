# 📦 Discord Server Logger & Cloner Bot

This bot clones the structure of a source Discord server into a logging server (categories, text channels, voice channels) and **logs all messages** (new, edited, deleted) into the corresponding channels in the logging server.

✅ Logs **all** messages
✅ Clones **categories, text channels, and voice channels**
✅ Logs message **content, edits, deletions**, attachments, timestamps, author info
✅ Supports `/status` command in logging server
✅ Runs **24/7 on Replit** with a keep-alive server

---

## 🛠️ Setup Guide

### 1️⃣ Create Your Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** → Name it → Go to **Bot** → **Add Bot**
3. Enable **Message Content Intent** under **Privileged Gateway Intents**
4. Copy the **Bot Token** (you’ll need this for Replit)

### 2️⃣ Get Server and Channel IDs

1. In Discord, go to **User Settings → Advanced → Developer Mode → Enable**
2. Right-click your servers:

   * **Source Server** → Click **Copy Server ID**
   * **Logging Server** → Click **Copy Server ID**

### 3️⃣ Set Up Replit

1. Go to [Replit](https://replit.com) → Create a new **Python Repl**
2. Upload the following files:

   * `main.py` (the bot code)
   * `keep_alive.py` (you already have this from previous steps)
3. In Replit, open the **Secrets** tab (lock icon) and add:

   * `DISCORD_TOKEN` → Your bot token
   * `SOURCE_SERVER_ID` → The source server ID
   * `LOGGING_SERVER_ID` → The logging server ID

### 4️⃣ Install Libraries

In the Replit **Shell**, run:

```bash
pip install discord.py
```

If `Flask` is not installed:

```bash
pip install Flask
```

### 5️⃣ Run Your Bot

In Replit, click **Run**.
✅ The Replit console should say **Bot is online** and the server will be cloned.

---

## 🌐 Keep Bot Online 24/7 (UptimeRobot)

1. Go to [UptimeRobot](https://uptimerobot.com/)
2. Create a free account → Add **New Monitor**:

   * Type: HTTP(s)
   * URL: Your Replit web URL (it appears in the console when you run)
   * Interval: 5 minutes
3. Done! Your bot will stay online.

---

## 📝 Commands

* `/status` → Responds with "I’m online!" (in logging server only)

---

## 🔍 What It Logs

✅ New messages
✅ Edited messages (with old content)
✅ Deleted messages
✅ Attachments (files/images)
✅ Author name & profile picture
✅ Timestamp
✅ Channel structure stays organized

---

## 🚫 Limitations

* The bot only works in the logging server after it clones the source structure.
* It only logs **text messages** in text channels (not voice activity or threads).
