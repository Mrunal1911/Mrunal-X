# made by @Alain_Champion and TEAMLEGEND
# Credites :- @Godmrunal , @PROBOYX
# if you kang this please keep credits

# SPECIES THANKS TEAMLEGEND

import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from userbot import bot
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
import io
from platform import python_version, uname
@bot.on(admin_cmd(pattern="wish ?(.*)"))
async def LEGENDBOT(event):
    LEGENDX = event.pattern_match.group(1)
    PROBOY = random.randint(0, 100)
    if LEGENDX:
        reslt = f'''๐ฆ Yแดแดส แดกษชsส สแดs สแดแดษด แดแดsแดแดแด ๐ฆ\n\n\nโ๏ธ ๐๐จ๐ฎ๐ซ ๐๐ข๐ฌ๐ก โช **`{LEGENDX}`** โจ
              \n\n๐ฅ๐ฒ๐ท๐ฐ๐ฝ๐ฒ๐ด ๐พ๐ต ๐๐๐ฒ๐ฒ๐ด๐๐ : **{PROBOY}%**'''
    else:
        if event.is_reply:
            reslt = f"๐ฆ Yแดแดส แดกษชsส สแดs สแดแดษด แดแดsแดแดแด ๐ฆ\
                 \n\n๐ฅ๐ฒ๐ท๐ฐ๐ฝ๐ฒ๐ด ๐พ๐ต ๐๐๐ฒ๐ฒ๐ด๐๐ : {PROBOY}%"
        else:
            result = f"๐ฆ Yแดแดส แดกษชsส สแดs สแดแดษด แดแดsแดแดแด ๐ฆ\
                  \n\n๐ฅ๐ฒ๐ท๐ฐ๐ฝ๐ฒ๐ด ๐พ๐ต ๐๐๐ฒ๐ฒ๐ด๐๐ : {PROBOY}%"
    await edit_or_reply(event, reslt)

CMD_HELP.update(
    {
        "wish": "**Plugin : **`wish`\
    \n\n**Syntax : **`.wish <your wish>`\
    \n**Function : **wish plug-in like .wish i am pro"
    }
)

