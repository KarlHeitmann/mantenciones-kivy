from kivy.app import App

from login import Login
from webserver import WebServer


class MantencionesApp(App):
    def build(self):
        self.ws = WebServer("http://192.168.43.150:5000", 1)
        return Login()


if __name__ == '__main__':
    MantencionesApp().run()
