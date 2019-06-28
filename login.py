from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from webserver import WebServer


class Login(Screen):
    domain_url = StringProperty()
    ws = None

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        print("__INIT__")

    def on_enter(self):
        # "192.168.43.150:5000"
        print("ON ENTER de login")

    def make_login(self):
        print("HACIENDO LOGIN")
        print(self.ids["ti_email"])
        print(self.ids["ti_email"].text)
        print(self.ids["ti_password"])
        print(self.ids["ti_password"].text)
        App.get_running_app().ws.login(self.ids["ti_email"].text, self.ids["ti_password"].text, _on_success=self.exito_login)

    def exito_login(self, req, result):
        print("===== VIENTO!!! =========")
        print(result)
        pass




