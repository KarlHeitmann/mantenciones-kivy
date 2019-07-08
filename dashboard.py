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
            informe_key = 'informe_' + str(self.grupo["id"])
            if App.get_running_app().store.exists(informe_key):
                mantencion_actual = "Tiene un informe de mantencion sin enviar"
            else:
                mantencion_actual = "Ningún informe de mantención pendiente"
            try:
                texto = ""
                texto = texto + ("[b]Marca:[/b] %s\n" %(self.grupo["marca"]))
                texto = texto + ("[b]Potencia:[/b] %s\n" %(self.grupo["potencia"]))
                texto = texto + ("[b]Número de serie:[/b] %s\n" %(self.grupo["numero_de_serie"]))
                texto = texto + ("[b]Modelo:[/b] %s\n" %(self.grupo["modelo"]))
                texto = texto + ("Tiene historial de mantenciones\n" if self.grupo["tiene_mantenciones"] else "No tiene historial de mantenciones\n")
                texto = texto + ("Toca hacer una mantención\n" if self.grupo["toca_mantencion"] else "No necesita mantención\n")
                texto = texto + '\n\n' + mantencion_actual
                self.ids["lbl_main"].text = texto

            except ValueError:
                print("Error de value")
            App.get_running_app().set_informe_actual('')
        else:
            self.ids["lbl_main"].text = "Ningún grupo ha sido seleccionado"

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

