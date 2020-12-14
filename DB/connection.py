from pymongo import MongoClient

def sendInfo(data,url):
    cliente = MongoClient(url)
    db = cliente['play_online']
    db.games.insert_one(data)

def getInfo(data,url):
    cliente = MongoClient(url)
    db = cliente['play_online']
    games = db.games.find(data)
    return games

def createUser(data, url):
    cliente = MongoClient(url)
    db = cliente['play_online']
    duplicated = db.users.find({"email" : data["email"]})
    if duplicated.count() == 0:
        db.users.insert_one(data)
        return True
    else:
        return False

def login(data, url):
    cliente = MongoClient(url)
    db = cliente['play_online']
    duplicated = db.users.find({"email" : data["email"]})
    if duplicated.count() > 0:
        return list(duplicated)[0]
    else:
        return False