import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 123456)
  API_HASH = os.environ.get("API_HASH", "")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
  SUDO_USERS.append(1204927413)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Coffe Joiner**\n\n**ئەندامانی گرووپ ناچار دەکات جۆینی کەناڵی گرووپ بکەن لەکاتی ناردنی نامە لە گرووپ چات.\n\n 🔇 ئەگەر هاتو ئەندامی گرووپ جۆینی کەناڵی گرووپی نەکردبێت من مافی چاتەکەی نا چاڵاک دەکەم\n\n هاوکات ئاگاداری دەکەمەوە لەوەی دەبێت جۆینی کەناڵی گرووپ بکات و دواتر چاتەکەت چاڵاک بکات.**",
        
        "**✅شێوازی کارا کردن✅**\n\n➕سەرەتا من زیاد زیادم بکە لە گرووپەکە و بمکە بە ئەدمین لە گرووپەکەت و کەناڵەکەت.\n\nتێبینی: تەنها ئەدمینی گشتی گرووپ یان کەناڵەکە دەتوانێت من بەکار بهێنێت ئەگەر هاتوو ڕۆڵی ئەدمینیم پێ نەدرابێت ناچار دەبم گرووپەکە جێبێڵم.**",
        
        "**⚙️فرمانەکان⚙️**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no یان off یانdisable - بۆ نا کارا کردنی بۆت\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nتێبینی: دەتوانیت فرمانی /coffe بەکار بێنیت وەک کورت کراوەیەک لە جیاتی/coffejoin**",
        
       "**داهێنراوە لە لایەن @MrMamo007.**"
      ]
    #  SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**بەخێربێیت [{}](tg://user?id={})**\n__من دەتوانم ئەندامەکان ناچار بکەم جۆینی کەناڵێکی * بکەن پێش نووسینی نامەکان لە گروپەکە.\nزانیاری زیاتر بزانە لە /help__"
