import falcon
import json

class CardsResource:

    def __init__(self, data):
        self.data = data
    
    def on_get(self, req, resp, user_id):
        try:
            result = self.data.get_cards(user_id=user_id)
        except exceptions.UserNotFoundError as ex:
            raise falcon.HTTPServiceUnavailable('', ex.message, 30)
        
        resp.media = result
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200