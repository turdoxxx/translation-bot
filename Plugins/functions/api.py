import requests 



# CHECK MEMEBER JOIN CHANNLS
async def CHECK_JOIN_MEMBER(user_id: int, channls: list, API_KEY: str):
    """
    user_id : The member telegram id 
    channls : list channls 
    API_KEY : Bot Token
    """
    states = ['administrator','creator','member','restricted']
    # Start Loop
    for channl in channls:
        try:
            api =f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id=@{channl}&user_id={user_id}"
            respons = requests.get(api).json()
            # Check Status 
            if respons['result']['status'] not in states:
                return (False, channl)
        except:
                return (False, channl)

    return (True, None)
