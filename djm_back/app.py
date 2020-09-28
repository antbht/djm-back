import falcon

from djm_back import storage

class DjmBack(falcon.API):

    def __init__(self):
        super().__init__(middleware=[])

        data = storage.MockStorage()
