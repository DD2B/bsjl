import asyncio
import os
import re

from pyrogram import Client, filters
from pyrogram.types import (
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

rid = Client(
    "Bot",
    api_id = 17003075,
 api_hash = "73a168d0a5a0d300236136c9c99e2063",
 bot_token = "5461333115:AAElLZMM9P7IiGAS7EwuPiD7wmKsDteZQ-4"
)

@rid.on_message(filters.command("رد", [".", ""]) & filters.user(5519275568))
async def owner(client, message):
        user_id = " ".join(message.command[1:])
        text = message.reply_to_message.text
        await rid.send_message(user_id, text)
        await message.reply_text("- تم ارسال رسالتك بنجاح ")
        
@rid.on_message(filters.command("start") & filters.private)
async def start(client, message):
       OWNER = 5519275568
       own = await client.get_chat(5519275568)
       name = own.first_name
       await rid.send_message(message.chat.id, f"**- مرحبًا بك في روبوت الاتصالات الخاص بــ ( [{name}](tg://user?id={OWNER}) )**\n**- أرسل رسالتك وسوف نقوم بالرد في أقرب وقت ممكن**\n**- شكرا لك على استخدام هذا الروبوت **.",
       reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "my official account .",
                        url=f'https://t.me/XRZOC'),
                        ],[
                            InlineKeyboardButton(
                        "Store Ricklss .",
                        url=f'https://t.me/JJCDT'),
                        ],
                    ]
                )
            ) 
       await rid.send_message(5519275568, f"**- شخص ما قام بتسجيل الدخول إلى الروبوت الخاص بك .**\n\n**- الاسم الشخص ( {message.from_user.mention} ) .**\n**- ايدي الشخص الدخل الروبوت** : `{message.from_user.id}` .")
       

@rid.on_message(filters.text & filters.private)
async def tawasol(client, message):
       OWNER = [5519275568]
       if message.from_user.id in OWNER:
         return
       await rid.send_message(5519275568, f"**- Message from ( {message.from_user.mention} ).**\n**- user Account :** ( @{message.from_user.username} )\n**- ID User :** ( `{message.from_user.id}` )\n\n**- message : {message.text}**\n\n- للرد عليه فقط ارسل رسالتك وقم بالرد على رسالتك بالأمر التالي [رد + يوزر الشخص او ايديه] ")       
             





print("Work⚡")
rid.run()
