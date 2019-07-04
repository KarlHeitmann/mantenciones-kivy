from kivy.app import App
from kivy.uix.screenmanager import Screen


class Historial(Screen):
    def btn_buscar(self):
        print(self.ids["ti_busqueda"].text)
        grupo_id = App.get_running_app().get_grupo_actual()
        print(grupo_id)

