from djm_back import exceptions
import unittest

from djm_back import storage, exceptions

class MockStorageTests(unittest.TestCase):
    def test_get_users(self):
        """ It should return a list of users which all have id, firtname and lastname"""
        data = storage.MockStorage()

        users = data.get_users()

        self.assertIsInstance(users, list)

        res = True
        for user in users:
            res = res and ('id' in user) and ('firstname' in user) and ('lastname' in user)
        self.assertTrue(res)

    def test_get_user(self):
        """ Get a user with its id should return all the information about the user"""
        data = storage.MockStorage()
        expected_res = {
            'id': '1234', 
            'firstname': "Arthur", 
            'lastname': "PENDRAGON",
            'cards': [
                {
                    'id':'9123456789123456',
                    'hidden_pan': 'XXXXXXXXXXXX1234'
                }
            ]
        }
        self.assertDictEqual(expected_res, data.get_user(expected_res['id']))

    
    def test_get_user_error(self):
        """ Get a user with a not existing id should raise an error"""
        data = storage.MockStorage()
        with self.assertRaises(exceptions.UserNotFoundError):
            data.get_user("NOT_EXIST")
    
    def test_get_cards(self):
        """ It should return the list of cards for a given user."""
        data = storage.MockStorage()
        expected_res = [
            {
                'id':'9123456789123456',
                'hidden_pan': 'XXXXXXXXXXXX1234'
            }
        ]
        self.assertListEqual(expected_res, data.get_cards(user_id='1234'))

    def test_get_cards_user_error(self):
        """ It should raise an error if the given user is not exist."""
        data = storage.MockStorage()
        with self.assertRaises(exceptions.UserNotFoundError):
            data.get_cards("NOT_EXIST")

        
    def test_add_card(self):
        """ It should add a card into the user ones and should return the new list"""
        data = storage.MockStorage()

        res = data.add_card('1234', '1234567891234567')
        expected_res = 'XXXXXXXXXXXX4567'
        self.assertEqual(res[-1]['hidden_pan'], expected_res)
        self.assertIn('id', res[-1])
        
        data = storage.MockStorage()

        res = data.add_card('1234', card)
        expected_res = [
            {
                'id':'9123456789123456',
                'hidden_pan': 'XXXXXXXXXXXX1234'
            },
            {
                'id':'789123456789',
                'hidden_pan': 'XXXXXXXXXXXX4567'
            }
        ]
        self.assertListEqual(res, expected_res)
        