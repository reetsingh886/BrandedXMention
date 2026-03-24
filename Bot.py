import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)  # ✅ fix

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")
    
    await event.client.send_file(
        event.chat_id,
        file="https://files.catbox.moe/rjk5ma.jpg",
        caption="━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ ɪ ᴀᴍ ᴀʟᴇxᴀ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ\n✪ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʀᴜɴ /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ ᴏᴡɴᴇʀ    : [ ʙᴏᴛ](https://t.me/BOTxBOOSTER)\n┣★ ᴜᴘᴅᴀᴛᴇs › : [ ʜᴇʟᴘ](https://t.me/BOTxBOOSTER)┓\n┣★ ʀᴇᴘᴏ › : [ ʀᴇᴘᴏ](https://t.me/BOTxBOOSTER)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ\nᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/iamthakur007) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=[
            [Button.url("❤️‍🔥 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 💫", "https://t.me/Branded_MentionBot?startgroup=true")],
            [Button.url("❤️‍🔥 ɢʀᴏᴜᴘ 💫", "https://t.me/BOTxBOOSTER"), Button.url("❤️‍🔥 ᴄʜᴀɴɴᴇʟ 💫", "https://t.me/BOTxBOOSTER")],
            [Button.url("❤️‍🔥 ʜᴇʀᴜᴋᴏ ᴄᴄ 💫", "https://t.me/BOTxBOOSTER"), Button.url("❤️‍🔥 BRANDED ❤️‍🔥", "https://t.me/BOTxBOOSTER")]
        ]
    )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n✪ Example: /mentionall Good Morning!"
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ 💫", "https://t.me/BOTxBOOSTER"),
                Button.url("❤️‍🔥 ʏᴏᴜᴛᴜʙᴇ 💫", "https://t.me/BotsSupport_36"),
            ]
        ),
    )

@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs  ʙᴏᴛ\n✪ ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ ʙʀᴀɴᴅᴇᴅ\n✪ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ\n✪ ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ 💫", "https://t.me/BOTxBOOSTER"),
                Button.url("❤️‍🔥 ʏᴏᴜᴛᴜʙᴇ 💫", "https://t.me/BOTxBOOSTER"),
            ]
        ),
    )

# ⚠️ BAQI CODE SAME (mentionall, admin, cancel) — koi change nahi

print(">> ʙʀᴀɴᴅᴇᴅ ᴍᴇɴᴛɪᴏɴ BOT WORKING <<")
client.run_until_disconnected()
