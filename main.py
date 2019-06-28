import os

from kivy.app import App

from login import Login
from webserver import WebServer


class MantencionesApp(App):
    def build(self):
        # self.ws = WebServer("http://192.168.43.150:5000", 1)
        if 'MANTENCIONES_VERBOSE' in os.environ:
            verbose=1
        else:
            verbose=0
        if 'DEVELOPMENT_SERVER' in os.environ:
            domain_url='http://192.168.43.150:5000'
        else:
            domain_url='http://kheitmann.webfactional.com'
        self.ws = WebServer(domain_url, verbose)
        return Login()


if __name__ == '__main__':
    MantencionesApp().run()
