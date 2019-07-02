from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from informe import Informe


class LabelInfo(BoxLayout):
    label_string = StringProperty()

    def set_content(self, contenido):
        if contenido != None:
            self.ids["contenido_text"].text = contenido


class Grupo(Screen):
    #grupo = ObjectProperty()

    def on_enter(self, *largs):
        print("En grupo")
        self.grupo = App.get_running_app().store.get("current_grupo")["val"]
        self.ids["marca"].set_content(self.grupo["marca"])
        self.ids["potencia"].set_content(self.grupo["potencia"])
        self.ids["numero_de_serie"].set_content(self.grupo["numero_de_serie"])
        self.ids["modelo"].set_content(self.grupo["modelo"])

        App.get_running_app().set_informe_actual('')

        print(self.grupo)

    def btn_on_reposo(self):
        if not(App.get_running_app().store.exists('informe')):
            App.get_running_app().store.put('informe',
                                            prueba_en_reposo={},
                                            prueba_manual={},
                                            prueba_automatico={})
        App.get_running_app().set_informe_actual('prueba_en_reposo')
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'prueba_en_reposo'


    def btn_on_manual(self):
        if not(App.get_running_app().store.exists('informe')):
            App.get_running_app().store.put('informe',
                                            prueba_en_reposo={},
                                            prueba_manual={},
                                            prueba_automatico={})
        App.get_running_app().set_informe_actual('prueba_manual')
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'prueba_manual'


    def btn_on_automatico(self):
        if not(App.get_running_app().store.exists('informe')):
            App.get_running_app().store.put('informe',
                                            prueba_en_reposo={},
                                            prueba_manual={},
                                            prueba_automatico={})
        App.get_running_app().set_informe_actual('prueba_automatico')
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'prueba_automatico'


if __name__ == '__main__':
    class GrupoApp(App):
        def build(self):
            self.screen_manager = ScreenManager()
            import os
            if 'MANTENCIONES_VERBOSE' in os.environ:
                verbose=1
            else:
                verbose=0
            if 'DEVELOPMENT_SERVER' in os.environ:
                # domain_url='http://192.168.43.150:5000'
                domain_url='http://192.168.1.39:5000'
            else:
                domain_url='http://kheitmann.webfactional.com'
            from webserver import WebServer
            from kivy.storage.jsonstore import JsonStore
            self.ws = WebServer(domain_url, verbose)
            self.store = JsonStore('base_de_datos.json')

            if self.store.exists('session'):
                session = self.store.get('session')
                if session['auth_token'] is None:
                    print("AUTH TOKEN ES NONE")
                    return None
                else:
                    self.ws.set_auth_token(session['auth_token'])
            else:
                print("NO HAY BASE DE DATOS")
                return None

            self.screen_manager.add_widget(Grupo(name='grupo'))
            self.screen_manager.add_widget(Informe(name='informe'))

            return self.screen_manager

    GrupoApp().run()

