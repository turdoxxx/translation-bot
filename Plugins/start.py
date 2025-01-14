# Requier Modules
from pyrogram import Client as app , filters, types 

# Requier BOt PLugins 
from config import Config, databesas
from helpers import Message, Keyboard
from Plugins.functions import api

@app.on_message(filters.private & filters.regex('^/start$'))
async def ON_START_BOT(app: app, message: types.Message):
    # check Join 
    Status, channl = await api.CHECK_JOIN_MEMBER(message.from_user.id, Config.CHANNLS, Config.API_KEY)
    if not Status:
        await app.send_message(
            chat_id=message.chat.id, 
            text=Message.HOME_MESSAGE['JOIN_CHAT'].format(channl),
            reply_markup=types.InlineKeyboardMarkup([[
                types.InlineKeyboardButton(text="↫ CH", url=f"t.me/{channl}")
            ]])
        )
        return
    
    # Check user Data
    if not databesas.USER_EXISTS(str(message.from_user.id)):
        await app.set_bot_commands([types.BotCommand('start', 'بدء التشغيل')])
        databesas.ADD_NEW_USER(str(message.from_user.id))
        await app.send_message(
            chat_id=Config.SUDO, text=Message.ADMIN_MESSAGE['NEWUSER'].format(message.from_user.id, message.from_user.username, message.from_user.first_name, len(databesas.GET_DATA()['users']))
        )

    # start bot 
    await app.send_message(
        chat_id=message.chat.id, 
        text=Message.HOME_MESSAGE['HOME_MESSAGE'], 
        reply_markup=Keyboard.Keyboard.HOME_KEYBOARD(message.from_user.id)
    )

