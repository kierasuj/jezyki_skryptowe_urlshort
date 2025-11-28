from database.db_service import MongoDBService
from utlis.id_generator import IdGenerator

def get_url(id: str):
    MongoDBService_instance = MongoDBService.get_instance()
    url_data = MongoDBService_instance.get_url(id)
    if url_data:
        return url_data["original_url"]
    
def save_url(original_url: str):
    MongoDBService_instance = MongoDBService.get_instance()
    id = IdGenerator.get_instance().next_id()
    MongoDBService_instance.save_url(id, original_url)