from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from decoradores import siguiente_trans, siguiente_trans_tres
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

    @siguiente_trans
    def make_login(self):
        print("HACIENDO LOGIN")
        print(self.ids["ti_email"])
        print(self.ids["ti_email"].text)
        print(self.ids["ti_password"])
        print(self.ids["ti_password"].text)
        App.get_running_app().ws.login(self.ids["ti_email"].text, self.ids["ti_password"].text,
                                       _on_success=self.exito_login, _on_failure=self.failure_login,
                                       _on_error=self.error_login)

    def exito_login(self, req, result):
        print("===== VIENTO!!! =========")
        print(result)
        App.get_running_app().ws.set_auth_token(result['auth_token'])
        App.get_running_app().store.put('session', auth_token=result["auth_token"], tipo="user")

        self.manager.current = 'dashboard'
        pass

    def failure_login(self, req, result):
        print("MAL, error en server")
        print(result)

    def error_login(self, req, result):
        print("Algo se hizo mal en la peticion")
        print(result)

    def resetForm(self):
        self.ids['ti_email'].text = ""
        self.ids['ti_password'].text = ""





