from pymongo import MongoClient

def enviarInfo(data,url):
    cliente = MongoClient(url)
    db = cliente['play_online']
    db.datos_naves.insert_one(data)