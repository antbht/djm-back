import uuid

from djm_back import exceptions

class MockStorage:

    def __init__(self):
        self.users = [
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
            },
            {
                'id': '9123', 
                'firstname': "Karadoc", 
                'lastname': "DE VANES",
                'cards': [
                    {
                        'id':'1234',
                        'hidden_pan': 'XXXXXXXXXXXX5678'
                    }
                ]
            } 
        ]

    def get_users(self):
        return self.users
    
    def get_user(self, id):
        for user in self.get_users():
            if user['id'] == id:
                return user
        raise exceptions.UserNotFoundError(f"You are asking for a user with id {id} which is not existing.")

    def get_cards(self, user_id):
        user = self.get_user(user_id)
        return user['cards']

    def add_card(self, user_id, card_pan):
        card_to_add = {
            'id': str(uuid.uuid1()),
            'hidden_pan': 'X'*12+card_pan[-4:]
        }
        user = self.get_user(user_id)
        user["cards"].append(card_to_add)
        return user["cards"]
    
    def delete_card(self, user_id, card_id):
        user = self.get_user(user_id)

        to_remove = -1
        for i in range(0,len(user["cards"])):
            card = user["cards"][i]
            if card["id"] == card_id:
                to_remove = i
        
        if to_remove != -1:  
            user["cards"].pop(to_remove)
            return card_id
        
        raise exceptions.CardNotFoundError(f"The card {card_id} is not existing for the user {user_id}")
