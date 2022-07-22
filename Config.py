import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5513383503:AAEMO-6X9euYKpAOpI7YvWG9kq0a87pylec")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/mrjoiners")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://mrjoiner:mrjoiner@139.185.39.186:5432/joiner")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 15545287)
  API_HASH = os.environ.get("API_HASH", "3b8958953958cb9329da0e96adab5f2a")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1203639446").split()))
  SUDO_USERS.append(1203639446)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\nForce group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**Devloped By @aboutez**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**بەخێربێیت [{}](tg://user?id={})**\n__من دەتوانم ئەندامەکان ناچار بکەم جۆینی کەناڵێکی دیاریکراو بکەن پێش نووسینی نامەکان لە گروپەکە.\nزانیاری زیاتر بزانە لە /help__"
