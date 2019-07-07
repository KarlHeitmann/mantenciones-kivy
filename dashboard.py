from kivy.app import App
from kivy.uix.screenmanager import Screen

from decoradores import volver_trans, arriba_trans, abajo_trans, siguiente_trans


class Dashboard(Screen):
    def on_enter(self, *largs):
        print("En grupo")
        # self.grupo = App.get_running_app().store.get("current_grupo")["val"]
        self.grupo = App.get_running_app().get_grupo_actual()

        #App.get_running_app().ws.

        print(self.grupo)
        if not(self.grupo is None):
            try:
                self.ids["marca"].text = self.grupo["marca"]
                self.ids["potencia"].text = self.grupo["potencia"]
                self.ids["numero_de_serie"].text = self.grupo["numero_de_serie"]
                self.ids["modelo"].text = self.grupo["modelo"]
            except ValueError:
                print("Error de value")
            App.get_running_app().set_informe_actual('')

        print(self.grupo)

    @volver_trans
    def btn_cerrar_sesion(self):
        App.get_running_app().store.put('session', auth_token=None, tipo=None)
        # App.get_running_app().store.async_put(self.callback_put_grupo, "current_grupo", val=self.grupos_bruto[index_data])
        App.get_running_app().store.put("current_grupo", val=None)
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    @abajo_trans
    def goto_historial(self):
        self.manager.current = 'historial'

    @arriba_trans
    def goto_grupos(self):
        self.manager.current = 'grupos'

    @siguiente_trans
    def goto_informe(self):
        self.manager.current = 'grupo'

