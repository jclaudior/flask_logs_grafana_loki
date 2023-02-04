from src.utils.mongo import client
from dataclasses import dataclass
from pymongo import ReturnDocument
from bson.objectid import ObjectId

CLIENT = client['user']

@dataclass
class UserModel:
    name: str
    birth: str
    id: str = ''
    

    def save(self):
        self.id = str(CLIENT.insert_one({"name": self.name, "birth": self.birth}).inserted_id)
        return self.serialize()
    
    def update(self):
        mongo_obj = CLIENT.find_one_and_update({'_id':  ObjectId(self.id)},{'$set': self.serialize()}, return_document=ReturnDocument.AFTER)
        return UserModel.to_model(mongo_obj).serialize()
    
    @staticmethod
    def get(id):
        objInstance = ObjectId(id)
        mongo_obj = CLIENT.find_one(objInstance)
        return UserModel.to_model(mongo_obj).serialize()
    
    @staticmethod
    def delete(id):
        return CLIENT.delete_one({'_id':  ObjectId(id)}).deleted_count

        
    @staticmethod
    def list():
        list = []
        mongo_list = CLIENT.find()
        for mongo_obj in mongo_list:
            list.append(UserModel.to_model(mongo_obj).serialize())
        return list


    def serialize(self):
        return {"id": self.id, "name": self.name, "birth": self.birth}
    
    @staticmethod
    def to_model(mongo_obj):
        return UserModel(id=str(mongo_obj['_id']), name=mongo_obj['name'], birth=mongo_obj['birth'])