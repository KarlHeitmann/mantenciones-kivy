from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.scrollview import ScrollView

from informe import Informe
from my_widgets import LabelInfo
from my_widgets import ScrollableLabel

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

    def pintar_scrollable_label(self, informe, llave):
        print(informe)
        print(informe[llave])
        texto = ""
        for prueba, reserva in informe[llave].items():
            texto = texto + prueba + ": " + reserva + "\n"
        self.ids["scrollable_label"].text=texto

    def ver_reposo(self):
        informe = App.get_running_app().store.get('informe')
        self.pintar_scrollable_label(informe, "prueba_en_reposo")
    def ver_manual(self):
        informe = App.get_running_app().store.get('informe')
        self.pintar_scrollable_label(informe, "prueba_manual")
    def ver_automatico(self):
        informe = App.get_running_app().store.get('informe')
        self.pintar_scrollable_label(informe, "prueba_automatico")



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

    def btn_volver(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'grupos'

    def btn_enviar(self):
        print("enviar")
        grupo = App.get_running_app().store.get('current_grupo')['val']

        pruebas = App.get_running_app().store.get('informe')
        App.get_running_app().ws.enviar_maintenance(grupo['id'],
                                                    pruebas['prueba_en_reposo'],
                                                    pruebas['prueba_manual'],
                                                    pruebas['prueba_automatico'],
                                                    _on_success=self.success_envio_informe
                                                    )
    def success_envio_informe(self, req, result):
        print("Exito al envio")
        print(result)

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

