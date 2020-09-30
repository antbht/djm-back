import argparse
import gunicorn.app.base

from djm_back import app


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="The IP of the expose backend api.", default="127.0.0.1",)
    parser.add_argument("--port", help="The PORT of the expose backend api.", default="8000")
    args = parser.parse_args()

    api_ip = args.host
    port = args.port

    options = {
        'bind': '%s:%s' % (api_ip, port),
    }
    StandaloneApplication(app.DjmBack(), options).run()

    