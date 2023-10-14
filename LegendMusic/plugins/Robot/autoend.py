from pyrogram import filters

import config
from strings import get_command
from LegendMusic import app
from LegendMusic.misc import SUDOERS
from LegendMusic.utils.database import autoend_off, autoend_on
from LegendMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**➻ ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "➻ အလိုအလျှောက်ပိတ်သောစနစ်ဖွင့်ပြီးပါပြီ။\n\nᴀssɪsᴛᴀɴᴛ သည် နားထောင်သူတစ်ဦးမှမရှိလျှင် သတိပေးအချက်ပြပြီး အလိုအလျှောက်ထွက်မည်ဖြစ်ပါသည်။"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("အလိုအလျှောက်ပိတ်သည့်စနစ်အား ပိတ်လိုက်ပါပြီ။")
    else:
        await message.reply_text(usage)
