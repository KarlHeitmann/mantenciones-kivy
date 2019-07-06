from kivy.app import App
from kivy.uix.screenmanager import Screen

from decoradores import arriba_trans


class Historial(Screen):
    def btn_buscar(self):
        print(self.ids["ti_busqueda"].text)
        grupo_id = App.get_running_app().get_grupo_actual()
        App.get_running_app().ws.buscar_maintenance(grupo_id, self.ids["ti_busqueda"].text, _on_success=self.callback_historial_success)
        print(grupo_id)

    def callback_historial_success(self, req, result):
        print(result)

    @arriba_trans
    def volver(self):
        self.manager.current = 'dashboard'