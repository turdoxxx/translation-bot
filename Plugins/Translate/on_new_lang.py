from pyrogram import Client as app , filters, types 
import googletrans
from googletrans import Translator

# Requier Bot Plugins
from config import databesas
from Plugins.Translate import Langsh
from helpers import Message, Keyboard


# on edit lang 
@app.on_callback_query(filters.regex('^from_lang$') | filters.regex('^to_lang$'))
async def ON_SHOW_LANGSH(app: app, query: types.CallbackQuery):
    _type = 'from' if query.data == 'from_lang' else 'to' 
    # edit message 
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id,
        text=Message.HOME_MESSAGE['SELECT_LANG'], reply_markup=Keyboard.Keyboard.SHOW_LANGSH(query.from_user.id,_type)
    )


# select lang 
@app.on_callback_query(filters.regex('^SELECT_LANG'))
async def ON_SELECT_LANGSH(app: app, query: types.CallbackQuery):
    CALL_SPLIT = query.data.split('|')
    LANG_LIST = Langsh.GET_LANGISH_LIST(CALL_SPLIT[1])
    usersdata = databesas.GET_DATA()
    usersdata['users'][str(query.from_user.id)]['lang'][CALL_SPLIT[1]] = LANG_LIST[CALL_SPLIT[2]]
    databesas.UPDATE_DATA(usersdata)
    # BACK HOME 
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['HOME_MESSAGE'], reply_markup=Keyboard.Keyboard.HOME_KEYBOARD(query.from_user.id)
    )