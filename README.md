# 📄 README: Discord Channel Logger Bot

This project is a **Discord bot** built with **Python** and **discord.py**, designed to:

✅ Clone channels from a **source server** to a **logging server**
✅ Log **all messages** (new, edited, deleted)
✅ Include **author info, message link, timestamp, and attachments**
✅ Include a **/status** command to check if the bot is online
✅ Use **Flask** to stay online 24/7 with **UptimeRobot**

---

## 🌐 How to Set Up

### 1️⃣ Create a Discord Bot

* Go to the [Discord Developer Portal](https://discord.com/developers/applications)
* Click **New Application** → Give it a name
* Go to **Bot** → **Add Bot**
* Click **Reset Token** → **Copy the token** (you’ll use this later as `DISCORD_TOKEN`)

---

### 2️⃣ Get Your Server & Channel IDs

1. Enable **Developer Mode** in Discord:

   * Settings → Advanced → Developer Mode → ON
2. Right-click your source server → **Copy Server ID**
3. Right-click your logging server → **Copy Server ID**

You’ll use these for:

* `SOURCE_SERVER_ID` = Your source server where users chat
* `LOGGING_SERVER_ID` = Your logging server where logs go

---

### 3️⃣ Set Up Replit Project

1. Go to [Replit](https://replit.com/) → Create a new **Python** repl
2. Add the files:

   * `main.py` (your bot code)
   * `keep_alive.py` (Flask server code)
3. Install libraries:

   * In the Replit **Shell**, type:

     ```
     pip install discord.py flask
     ```
4. Create **Secrets** in Replit:

   * Go to **Secrets (Lock icon)** on the left side
   * Add these:

     ```
     DISCORD_TOKEN = your bot token
     SOURCE_SERVER_ID = your source server ID (number)
     LOGGING_SERVER_ID = your logging server ID (number)
     ```

---

### 4️⃣ UptimeRobot Setup (Keep Bot Online 24/7)

1. Go to [UptimeRobot](https://uptimerobot.com/) → Sign up
2. Click **Add New Monitor**
3. Select **HTTP(s)**
4. For **URL**, paste your Replit URL:

   ```
   https://<your-repl-username>.<your-repl-name>.repl.co
   ```
5. Set interval (e.g., 5 minutes)
6. UptimeRobot will ping the Flask server → Replit won’t sleep → Bot stays online!

---

### 5️⃣ Run the Bot!

* Click the **Run** button in Replit
* Your bot will log:

  ```
  ✅ Bot is online as <BotName>
  ```
* Test it in Discord:

  * Send a message → It’s logged
  * Edit a message → It’s logged
  * Delete a message → It’s logged
  * Create or rename channels → It’s mirrored in the logging server!

---

## 📋 Commands

| Command   | What it does            |
| --------- | ----------------------- |
| `/status` | Replies "✅ I’m online!" |

---

## 🛡️ Features Summary

✅ Clone channels (create/rename)
✅ Log messages (new, edited, deleted)
✅ Include attachments
✅ Author info, message link, timestamp
✅ 24/7 uptime with UptimeRobot
✅ Error handling (basic)

---

### 🎓 Credits

Built with:

* Python
* discord.py
* Flask
* Replit

---

Let me know if you’d like a **markdown file** or a **PDF** version of the README! 📄
