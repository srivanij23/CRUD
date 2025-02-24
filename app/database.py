def get_db():
    client = MongoClient("mongodb://mongo:27017/")
    db = client["users_db"]
    return db