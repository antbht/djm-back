
from djm_back import exceptions

class MockStorage:

    def get_users(self):
        return [
            {
                'id': '1234', 
                'firstname': "Arthur", 
                'lastname': "PENDRAGON",
                'cards': [
                    {
                        'id':'9123456789123456',
                        'hidden_pan': 'XXXXXXXXXXXX1234'
                    }
                ]
            },
            {
                'id': '5678', 
                'firstname': "Perceval", 
                'lastname': "DE GALLES",
                'cards': [
                    {
                        'id':'7891234567891234',
                        'hidden_pan': 'XXXXXXXXXXXX5678'
                    },
                    {
                        'id':'5678912345678912',
                        'hidden_pan': 'XXXXXXXXXXXX9123'
                    }
                ]
            } 
        ]
    
    def get_user(self, id):
        for user in self.get_users():
            if user['id'] == id:
                return user
        raise exceptions.UserNotFoundError(f"You are asking for a user with id {id} which is not existing.")

    def get_cards(self, user_id):
        user = self.get_user(user_id)
        return user['cards']