from pymongo import MongoClient

client = MongoClient('mongodb+srv://kurniaramadhan:ttg3JzFNrL6LJfuq@cluster0.zb9ev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

doc = {
    'name': 'bob',
    'age': 27
}

db.users.insert_one(doc)