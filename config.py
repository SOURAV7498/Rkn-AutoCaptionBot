# AutoCaptionBot by RknDeveloper
# Copyright (c) 2024 RknDeveloper
# Licensed under the MIT License
# https://github.com/RknDeveloper/Rkn-AutoCaptionBot/blob/main/LICENSE
# Please retain this credit when using or forking this code.

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!


import os
import time

class Rkn_Botz(object):
    # Rkn client config (required)
    API_ID = os.environ.get("API_ID", "21140176")
    API_HASH = os.environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8381395008:AAFLu-Ytm0g6uhIBmAmsDgEvb7Fg6XPgtt4")

    # Start pic (default image link)
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")

    # Bot uptime (start time)
    BOT_UPTIME = time.time()

    # Server port (default 8080)
    PORT = int(os.environ.get("PORT", "8080"))

    # Force subscribe channel username (without @) (only public chats username required)
    FORCE_SUB = os.environ.get("FORCE_SUB", "Movieroll_M")

    # Database config (required)
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://gouravbolange_db_user:yos9d73FCsyLpiI6@cluster0.wxnzgc0.mongodb.net/?retryWrites=true&w=majority&AutoCaption=Cluster0")

    # Default caption (with safe fallback)
    DEFAULT_CAPTION = os.environ.get(
        "DEFAULT_CAPTION",
        "<b><a href='https://t.me/Movie_Provider_group'>{file_name}</a></b>

⚜️ <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <b><a href='https://t.me/+-dkKSAGoUf4wZGFl'>[ Movieroll ]</a></b>"
    )

    # Sticker ID default
    STICKER_ID = os.environ.get(
        "STICKER_ID",
        "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE"
    )

    # Admin ID (single integer)
    ADMIN = int(os.environ.get('ADMIN', '6222491731'))  # Yahan default ko apne Telegram User ID se replace karo

# ————
# End of file
# Original author: @RknDeveloperr
# GitHub: https://github.com/RknDeveloper

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support


# ⚠️ Please do not remove this credit!

