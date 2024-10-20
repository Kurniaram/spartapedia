from pymongo import MongoClient

client = MongoClient('mongodb+srv://kurniaramadhan:ttg3JzFNrL6LJfuq@cluster0.zb9ev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

target_movie = db.movies.find_one({'movie': 'The Matrix'})
print(target_movie['rating'])