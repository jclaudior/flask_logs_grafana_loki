from src.model.user_model import UserModel
from src.exceptions.user_exception import EmptyValueInAtribute, UserNotFountInDelete

class UserService():
    
    def list(self):
        return UserModel.list()

    def get_by_id(self, id):
       return UserModel.get(id)
    
    def save(self, data):
        name = data['name']
        birth = data['birth']
        if not name and not name.strip():
            raise EmptyValueInAtribute('Atribute name is empty')
        if not birth and not birth.strip():
            raise EmptyValueInAtribute('Atribute birth is empty')
        user = UserModel(name, birth)
        return user.save()
    
    def update(self, id, data):
        name = data['name']
        birth = data['birth']
        if not name and not name.strip():
            raise EmptyValueInAtribute('Atribute name is empty')
        if not birth and not birth.strip():
            raise EmptyValueInAtribute('Atribute birth is empty')
        user = UserModel(name, birth, id)
        return user.update()
    
    def delete(self, id):
        deleted = UserModel.delete(id)
        if deleted == 0:
            raise UserNotFountInDelete(f'User {id} not found in delete!')

    