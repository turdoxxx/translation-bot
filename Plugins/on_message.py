# Requier Modules
from pyrogram import Client as app , filters, types 
from googletrans import Translator

# Requier Bot Plugins
from config import  databesas

def IS_NOTCOMMAND(data):
    def func(flt, _, message: types.Message):
        if message.text != flt.data:
            return True 
        else: return False
    return filters.create(func, data=data)




# on text 
@app.on_message(filters.private & filters.text & IS_NOTCOMMAND('/start'))
async def ON_TRANS(app: app, message: types.Message):
    # get user data 
    usersdata = databesas.GET_DATA()
    userdata  = usersdata['users'][str(message.from_user.id)]
    # get text
    text = message.text
    # Tarns Obj 
    Trans = Translator()
    # get text dict 
    if userdata['lang']['from'] == 'auto':
        text_dict = Trans.detect(text)

    # start transslet
    Trasn_data = Trans.translate(
        text=text,
        dest=userdata['lang']['to'],
        src=userdata['lang']['from'],
    )
    # send Tarns 
    await app.send_message(
        chat_id=message.chat.id, reply_to_message_id=message.id, 
        text=Trasn_data.text
    )


    
