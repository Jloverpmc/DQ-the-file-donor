from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import F_SUB
import re

async def not_subscriber(_, client, message):
   if not client.f_channel:
      return False
   try:             
      user = await client.get_chat_member(client.f_channel, message.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != enums.ChatMemberStatus.BANNED:                       
         return False 
   return True

@Client.on_message(filters.create(not_subscriber))
async def is_not_subscribed(client, message):
    if message.text.startswith('/'): 
        buttons = [[InlineKeyboardButton(text="ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url="https://t.me/ALLNEWMOVIEZSCOM")]]
        text = f"sᴏʀʀʏ {message.from_user.mention}\nʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍʏ ʙᴏᴛ."
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    elif message.text: 
        buttons = [[InlineKeyboardButton(text="ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url="https://t.me/ALLNEWMOVIEZSCOM")]]
        text = f"sᴏʀʀʏ {message.from_user.mention}\nʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍʏ ʙᴏᴛ."
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
