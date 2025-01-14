# Requier Modules .
import googletrans


# LIST LANG
def GET_LANGISH_LIST(trans_type : str):
    LANG_LIST = {}
    LANSH = googletrans.LANGCODES

    # cehck trans type 
    if trans_type == 'from':
        LANG_LIST.update({'Auto':'auto'})
        [LANG_LIST.update({i:LANSH[i]}) for i in LANSH]
        return LANG_LIST
    
    return LANSH


