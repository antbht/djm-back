import falcon


class DjmBack(falcon.API):

    def __init__(self):
        super().__init__(middleware=[])

