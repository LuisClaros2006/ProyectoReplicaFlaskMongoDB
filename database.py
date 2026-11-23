from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://luisclarosr_db_user:7UsDWk6Lzs1fGDCZ@cluster0.wxp2rli.mongodb.net/'

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
