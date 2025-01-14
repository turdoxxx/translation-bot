from config import databesas
from Plugins.Translate import Langsh
from pyrogram import types

def CROVET_LIST_ITEMS(Dictes: dict, count_list: int):
    LISTS = []
    new_dict = {}
    [new_dict.update({k:i}) for k,i in enumerate(Dictes)]
    
    # starty loop 
    Items_id = 0
    for ii in range(int(len(new_dict)/count_list)+1):
        Lis = []
        # check 
        if len(new_dict)-Items_id < count_list:
            if len(new_dict)-Items_id == 0:
                break
            for i in range(len(new_dict)-Items_id):
                Lis.append(new_dict[Items_id])
                Items_id+=1
            LISTS.append(Lis)
            
            break
        
        for i in range(count_list):
            Lis.append(new_dict[Items_id])
            Items_id+=1
        LISTS.append(Lis)

    return LISTS


# HOME KEYBOARD 
class Keyboard:

    def HOME_KEYBOARD(user_id: int):
            userdata = databesas.GET_DATA()['users'][str(user_id)]
            LANGSH = Langsh.GET_LANGISH_LIST('from')
            LANG_LIST_FLATIER= {}
            [LANG_LIST_FLATIER.update({LANGSH[i]:i}) for i in LANGSH]
            return types.InlineKeyboardMarkup([
                  # [
                  #       types.InlineKeyboardButton("اختر الفات", "NOT"),
                  #       types.InlineKeyboardButton("من", "NOT"),
                  #       types.InlineKeyboardButton("الى", "NOT")
                  # ],[
                  [
                        types.InlineKeyboardButton("↫︙من", "NOT"),
                        types.InlineKeyboardButton(userdata['lang']['from'], "from_lang"),
                        types.InlineKeyboardButton(LANG_LIST_FLATIER[userdata['lang']['from']], "NOT")
                  ],[
                        types.InlineKeyboardButton("↫︙الى", "NOT"),
                        types.InlineKeyboardButton(userdata['lang']['to'], "to_lang"),
                        types.InlineKeyboardButton(LANG_LIST_FLATIER[userdata['lang']['to']], "NOT")
                  ]
            ])
    
    def SHOW_LANGSH(user_id: int, type: str):
          LANG_LIST = Langsh.GET_LANGISH_LIST(type)
          keyboards = []
          FILTER_LIST = CROVET_LIST_ITEMS(LANG_LIST, 5)
          for i in FILTER_LIST:
               KEs = []
               for ii in i: 
                    KEs.append(types.InlineKeyboardButton(ii, callback_data=f"SELECT_LANG|{type}|{ii}"))
               keyboards.append(KEs)
          keyboards.append([types.InlineKeyboardButton('BACK .', 'back')])
          return types.InlineKeyboardMarkup(keyboards)         
    


class ADMIN_KEYBOARD:

    def PANEL(USERS_COUNT: int, SESSIONS: int):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text=f'SESSIONS︙ ❲ {SESSIONS} ❳', callback_data='NOT'),
                types.InlineKeyboardButton(text=f'USERS    ︙ ❲ {USERS_COUNT} ❳', callback_data='NOT')
            ], 
            [
                types.InlineKeyboardButton(text='broadcasting', callback_data='ADMIN_BROADCASTING'),
                types.InlineKeyboardButton(text='NOT', callback_data='NOT')
            ]
        ])
    
    def BACK():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text='Back.', callback_data='BACK_ADMIN')
            ]
        ])