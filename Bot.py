import os, logging, asyncio
from telethon import Button, TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")

client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


# ================= START =================
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")

    await event.client.send_file(
        event.chat_id,
        file="https://files.catbox.moe/rjk5ma.jpg",
        caption="━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "✪ ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ 🤖\n"
                "✪ ɪ ᴄᴀɴ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ\n\n"
                "✪ ᴜsᴇ /ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━━",
        buttons=[
            [Button.url("❤️‍🔥 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 💫", "https://t.me/Branded_MentionBot?startgroup=true")],
            [
                Button.url("❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ 💫", "https://t.me/BotsSupport_36"),
                Button.url("❤️‍🔥 ᴜᴘᴅᴀᴛᴇs 💫", "https://t.me/BOTxBOOSTER")
            ],
            [
                Button.url("❤️‍🔥 ᴏᴡɴᴇʀ 💫", "https://t.me/iamthakur007")
            ]
        ]
    )


# ================= HELP =================
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    if not event.is_private:
        return await event.respond("ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ 🥺")

    helptext = (
        "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n"
        "✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n"
        "✪ ᴄᴏᴍᴍᴀɴᴅ: /utag\n"
        "✪ ᴄᴏᴍᴍᴀɴᴅ: @all\n"
        "✪ ᴄᴏᴍᴍᴀɴᴅ: /admin\n"
        "✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel\n\n"
        "✪ Example:\n"
        "/mentionall Good Morning\n"
        "/utag Hello\n"
        "@all Hi everyone"
    )

    await event.reply(helptext)


# ================= MENTION ALL =================
@client.on(events.NewMessage(pattern="^(/mentionall|/utag|@all) ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id

    if event.is_private:
        return await event.respond("ɢʀᴏᴜᴘ ᴏɴʟʏ ❌")

    try:
        p = await client(GetParticipantRequest(chat_id, event.sender_id))
        if not isinstance(p.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
            return await event.respond("ᴀᴅᴍɪɴ ᴏɴʟʏ ❌")
    except:
        return await event.respond("ᴀᴅᴍɪɴ ᴏɴʟʏ ❌")

    if event.pattern_match.group(2):
        user_text = event.pattern_match.group(2)
    elif event.is_reply:
        reply = await event.get_reply_message()
        user_text = reply.text if reply else ""
    else:
        return await event.respond("ɢɪᴠᴇ ᴛᴇxᴛ ❌")

    spam_chats.append(chat_id)

    count = 0
    text = ""
    done = 0

    async for user in client.iter_participants(chat_id):
        if chat_id not in spam_chats:
            break

        count += 1
        done += 1

        name = user.first_name or "User"
        text += f"⊙ [{name}](tg://user?id={user.id})\n"

        if count == 5:
            await client.send_message(
                chat_id,
                f"@all {user_text}\n\n{text}\n📢 TAGGING {done} USERS DONE...",
                link_preview=False
            )
            await asyncio.sleep(2)
            count = 0
            text = ""

    if text:
        await client.send_message(
            chat_id,
            f"@all {user_text}\n\n{text}\n📢 TAGGING {done} USERS DONE...",
            link_preview=False
        )

    spam_chats.remove(chat_id)


# ================= ADMIN TAG =================
@client.on(events.NewMessage(pattern="^(/admin|/admins|@admin|@admins) ?(.*)"))
async def admin_tag(event):
    chat_id = event.chat_id

    if event.is_private:
        return await event.respond("ɢʀᴏᴜᴘ ᴏɴʟʏ ❌")

    spam_chats.append(chat_id)

    count = 0
    text = ""
    done = 0

    async for user in client.iter_participants(chat_id, filter=ChannelParticipantsAdmins):
        if chat_id not in spam_chats:
            break

        count += 1
        done += 1

        name = user.first_name or "Admin"
        text += f"⊙ [{name}](tg://user?id={user.id})\n"

        if count == 5:
            await client.send_message(
                chat_id,
                f"Admins 👇\n\n{text}\n📢 TAGGING {done} ADMINS DONE...",
                link_preview=False
            )
            await asyncio.sleep(2)
            count = 0
            text = ""

    if text:
        await client.send_message(
            chat_id,
            f"Admins 👇\n\n{text}\n📢 TAGGING {done} ADMINS DONE...",
            link_preview=False
        )

    spam_chats.remove(chat_id)


# ================= CANCEL =================
@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel(event):
    if event.chat_id in spam_chats:
        spam_chats.remove(event.chat_id)
        await event.respond("sᴛᴏᴘᴘᴇᴅ ✅")
    else:
        await event.respond("ɴᴏ ᴘʀᴏᴄᴇss ❌")


print("🔥 BOT WORKING 🔥")
client.run_until_disconnected()
