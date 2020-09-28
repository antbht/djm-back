from djm_back import app

import gunicorn.app.base

class StandaloneApplication(gunicorn.app.base.BaseApplication):
    
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def main():
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8000'),
    }
    StandaloneApplication(app.DjmBack(), options).run()

    