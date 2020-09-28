import falcon

from djm_back import cards
from djm_back import storage


class DjmBack(falcon.API):

    def __init__(self):
        super().__init__(middleware=[])

        data = storage.MockStorage()


        res_cards = cards.CardsResource(data)
        self.add_route('/users/{user_id}/cards', res_cards)
