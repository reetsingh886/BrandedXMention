import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


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
        caption="━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "✪ ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇɴᴛɪᴏɴ ʙᴏᴛ 🤖\n"
                "✪ ɪ ᴄᴀɴ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ\n\n"
                "✪ ᴜsᴇ /ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs\n\n"
                "━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
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
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ 🥺")

    helptext = "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n" \
    "✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n" \
    "✪ ᴄᴏᴍᴍᴀɴᴅ: /utag\n" \
    "✪ ᴄᴏᴍᴍᴀɴᴅ: @all\n" \
    "✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n" \
    "✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n" \
    "✪ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.\n" \
    "✪ Example: /mentionall Good Morning!\n" \
    "✪ Example: /utag Hello\n" \
    "✪ Example: @all Hi everyone\n" \
    "✪ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ."

    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ 💫", "https://t.me/BRANDED_WORLD"),
                Button.url("❤️‍🔥 ʏᴏᴜᴛᴜʙᴇ 💫", "https://youtube.com/@TrickyBranded?si=LiWu6DkLNs4bcZn6"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def owner(event):
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ 🥺")

    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [ʙʀᴀɴᴅᴇᴅ ʙᴏᴛ](https://t.me/BRANDRD_BOT)\n✪ ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ ʙʀᴀɴᴅᴇᴅ\n✪ ʏᴏᴜᴛᴜʙᴇ [ᴄʜᴀɴɴᴇʟ](https://youtube.com/TrickyBranded)\n✪ ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ."

    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 ꜱᴜᴘᴘᴏʀᴛ 💫", "https://t.me/BRANDED_WORLD"),
                Button.url("❤️‍🔥 ʏᴏᴜᴛᴜʙᴇ 💫", "https://youtube.com/TrickyBranded"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^(/mentionall|/utag|@all) ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id

    if event.is_private:
        return await event.respond(
            "ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True

    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ")

    if event.pattern_match.group(2) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ ᴍᴇ ᴏɴᴇ ᴀʀɢᴜᴍᴇɴᴛ")

    elif event.pattern_match.group(2):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(2)

    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs!"
            )
    else:
        return await event.respond(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_participants(chat_id):
        if chat_id not in spam_chats:
            break

        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "

        if usrnum == 5:
            if mode == "text_on_cmd":
                await client.send_message(chat_id, f"{usrtxt}\n\n{msg}")
            else:
                await msg.reply(usrtxt)

            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)"
            )
    else:
        return await event.respond(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("sᴛᴏᴘᴘᴇᴅ.")


print(">> ʙʀᴀɴᴅᴇᴅ ᴍᴇɴᴛɪᴏɴ BOT WORKING <<")
client.run_until_disconnected()
    
