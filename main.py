import os

from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager

from grupo import Grupo
from grupos import Grupos
from informe import Informe
from login import Login
from webserver import WebServer

def agregar_screens(manager):
    manager.add_widget(Grupo(name='grupo'))
    manager.add_widget(Informe(name='informe'))

class MantencionesApp(App):
    def build(self):
        # self.ws = WebServer("http://192.168.43.150:5000", 1)
        self.screen_manager = ScreenManager()
        if 'MANTENCIONES_VERBOSE' in os.environ:
            verbose=1
        else:
            verbose=0
        if 'DEVELOPMENT_SERVER' in os.environ:
            domain_url='http://192.168.43.150:5000'
            # domain_url='http://192.168.1.39:5000'
        else:
            domain_url='http://kheitmann.webfactional.com'
        self.ws = WebServer(domain_url, verbose)
        self.store = JsonStore('base_de_datos.json')
        if self.store.exists('session'):
            session = self.store.get('session')
            if session['auth_token'] is None:
                print("No hay login")
                self.screen_manager.add_widget(Login(name="login"))
                self.screen_manager.add_widget(Grupos(name="grupos"))
            else:
                print("Si hay login")
                self.ws.set_auth_token(session['auth_token'])
                self.screen_manager.add_widget(Grupos(name="grupos"))
                self.screen_manager.add_widget(Login(name="login"))
        else:
            print("no hay")
            self.store.put('session', auth_token=None)
            self.screen_manager.add_widget(Login(name="login"))
            self.screen_manager.add_widget(Grupos(name="grupos"))
        agregar_screens(self.screen_manager)
        return self.screen_manager


if __name__ == '__main__':
    MantencionesApp().run()
