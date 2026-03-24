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
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")

client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)

spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
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
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n✪ Example: /mentionall Good Morning!"
    await event.reply(helptext, link_preview=False)


@client.on(events.NewMessage(pattern="^/owner$"))
async def owner(event):
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [ ʙᴏᴛ](https://t.me/BOTxBOOSTER)"
    await event.reply(helptext, link_preview=False)


# ADMIN CHECK
async def is_admin(event):
    try:
        p = await client(GetParticipantRequest(event.chat_id, event.sender_id))
        return isinstance(
            p.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        )
    except:
        return False


@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
    if event.is_private:
        return await event.respond("Use in groups only.")

    if not await is_admin(event):
        return await event.respond("Admins only!")

    msg = event.pattern_match.group(1)

    spam_chats.append(event.chat_id)

    users = ""
    count = 0

    async for user in client.iter_participants(event.chat_id):
        if event.chat_id not in spam_chats:
            break

        users += f"[{user.first_name}](tg://user?id={user.id}) "
        count += 1

        if count == 5:
            await client.send_message(event.chat_id, f"{users}\n\n{msg}")
            await asyncio.sleep(2)
            users = ""
            count = 0

    spam_chats.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel(event):
    if event.chat_id in spam_chats:
        spam_chats.remove(event.chat_id)
        await event.respond("Stopped ✅")
    else:
        await event.respond("No process running.")


print("🔥 BOT WORKING PERFECTLY 🔥")
client.run_until_disconnected()
