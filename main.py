import os

from kivy.app import App
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager

from dashboard import Dashboard
from grupo import Grupo
from grupos import Grupos
from informe import Informe
from login import Login
from webserver import WebServer

def agregar_screens(manager):
    manager.add_widget(Dashboard(name='dashboard'))
    manager.add_widget(Grupo(name='grupo'))
    manager.add_widget(Informe(name='prueba_en_reposo'))
    manager.add_widget(Informe(name='prueba_manual'))
    manager.add_widget(Informe(name='prueba_automatico'))

class MantencionesApp(App):
    def __init__(self, **kwargs):
        super(MantencionesApp, self).__init__(**kwargs)

        Window.bind(on_keyboard=self.Android_back_click)

    def set_informe_actual(self, _informe_actual):
        self.informe_actual = _informe_actual

    def get_informe_actual(self):
        return self.informe_actual

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
        self.informe_actual = ""
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

    def Android_back_click(self,window,key,*largs):
        # Codigo del boton back de android
        if key == 27:
            print("BACK!")
            # self.manager.transition = SlideTransition(direction="right")
            # self.manager.current = 'grupo'
            return True


if __name__ == '__main__':
    MantencionesApp().run()
