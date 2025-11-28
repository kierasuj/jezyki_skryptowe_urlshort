import singleton from decorators
from pymongo import MongoClient

@singleton
class MongoDBService:
    def __init__(self, host, port) -> None:
        self.db_client = MongoClient(f"mongodb://{host}:{port}/")

    def get_collection(self, collection_name: str):
        return self.db_client[collection_name]
    
    def get_url(self, id: str):
        collection = self.db_client["urls"]
        return collection.find_one({"id": id})
    
    def save_url(self, id: str, original_url: str):
        collection = self.db_client["urls"]
        collection.insert_one({"id": id, "original_url": original_url})
    
    def close_connection(self):
        self.db_client.close()

    