def createUser():
    nickname = ""
    email = ""
    password = ""
    return {"nickname" : nickname, "email" : email, "password" : password}

def login(data):
    nickname = data["nickname"]
    email = data["email"]
    password = data["password"]