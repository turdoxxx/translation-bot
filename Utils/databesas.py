# Requier Modules 
import json, os ,datetime


# databesas Class 
class Databesas:

    def __init__(self):
        self.PAT = 'databesas/usersdata.json'
        # data opj
        self.Obj = {
            'users':{}
        }
        # check data create
        if not os.path.exists(self.PAT):
            json.dump(self.Obj, open(self.PAT, 'w'), indent=3)

    # # Get All Data
    def GET_DATA(self):
        return json.load(open(self.PAT, 'r'))

    # UPDATE ALL DATA
    def UPDATE_DATA(self, NEW_DATA: dict):
        json.dump(NEW_DATA, open(self.PAT, 'w'), indent=3)

    # Add New User
    def ADD_NEW_USER(self, user_id: int):
        data = self.GET_DATA()
        data['users'].update({user_id:{
            "lang":{
                'from':'auto', 
                'to':'ar'
            }
        }})
        self.UPDATE_DATA(data)

    # def GET_USERS_DATA(self, user_id: int):
    #     return self.GET_DATA()['users'][user_id]

    # USer Exists
    def USER_EXISTS(self, user_id: int):
        return str(user_id) in self.GET_DATA()['users']

    


