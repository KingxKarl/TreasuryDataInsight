import pymongo

def store_data_in_mongodb(data, db_name, collection_name):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    if data:
        collection.insert_many(data)
