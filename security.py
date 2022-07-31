from user import User
users =[User(1,'bob','Itsmesoopen'),User(2,'ram','sudhARJUNAN')]

username_mapping = {}
userid_mapping = {}
for u in users:
    username_mapping[u.user_name] = u
    userid_mapping[u.user_id] =u

def auth(user_name,password):
    myuser = username_mapping.get(user_name, None)
    if user_name in username_mapping and myuser.password == password:
        return f"{user_name} authentication is sucessful"
def identity(payload):
    user_id = payload['identity']
    return username_mapping.get(user_id,None) #returns none if no userId is found
