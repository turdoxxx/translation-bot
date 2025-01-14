from pyrogram import Client as app , filters, types 
from pyromod.exceptions import ListenerTimeout

# Requier Helpers and plugin bot .
from config import databesas, Config
from helpers import Message, Keyboard


# admin start [/admin]
@app.on_message(filters.regex('^/admin$') & filters.private)
async def ADMIN_PANL(app: app, message :types.Message):
    if message.from_user.id != Config.SUDO:
        return
    userscount = len(databesas.GET_DATA()['users'])
    # sessionscount = jsdata.GET_DATA()['statistics']['sessions']
    await app.send_message(
        chat_id=message.chat.id,
        text=Message.ADMIN_MESSAGE['HOME'],
        reply_markup=Keyboard.ADMIN_KEYBOARD.PANEL(userscount, 0)
    )




# BACK 
@app.on_callback_query(filters.regex('^BACK_ADMIN$'))
async def BACK_ADMIN(app: app, query: types.CallbackQuery):
    userscount = len(databesas.GET_DATA()['users'])
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id ,
        text=Message.ADMIN_MESSAGE['HOME'], 
        reply_markup=Keyboard.ADMIN_KEYBOARD.PANEL(userscount)
    )


# On Callback Crovet 
@app.on_callback_query(filters.regex('^ADMIN_BROADCASTING$'))
async def ADMIN_BROADCASTING(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id ,
        text=Message.ADMIN_MESSAGE['BROADCASTING']
    )
    # on listing 
    try:
        response = await app.listen(
            chat_id=query.message.chat.id, 
            user_id=query.from_user.id,
            filters=filters.text,timeout=60
            )
    except ListenerTimeout as e:
        return
    broad_message = response.text
    
    # check message  and start broadcasting
    USERS_IDS = databesas.GET_DATA()['users'].keys()
    message_with = await app.send_message(
        chat_id=query.message.chat.id,
        text=Message.ADMIN_MESSAGE['START_BROADCASTING'].format(0,0, 'Looding'),
        reply_markup=Keyboard.ADMIN_KEYBOARD.BACK()

    )
    # start loops
    Trues, Falses = 0, 0
    for usersid in USERS_IDS:
        try:
            await app.send_message(
                chat_id=int(usersid), 
                text=broad_message, 
            ) 
            Trues+=1
            await app.edit_message_text(
                chat_id=query.message.chat.id,message_id=message_with.id,
                text=Message.ADMIN_MESSAGE['START_BROADCASTING'].format(Trues,Falses ,'Startings')
            )
        except Exception as Err:
            print(Err)
            Falses+=1
            await app.edit_message_text(
                chat_id=query.message.chat.id,message_id=message_with.id,
                text=Message.ADMIN_MESSAGE['START_BROADCASTING'].format(Trues,Falses, 'Startings')
            )

    await app.edit_message_text(
        chat_id=query.message.chat.id,message_id=message_with.id,
        text=Message.ADMIN_MESSAGE['START_BROADCASTING'].format(Trues,Falses, 'Done'),
        reply_markup=Keyboard.ADMIN_KEYBOARD.BACK()
    )




    
