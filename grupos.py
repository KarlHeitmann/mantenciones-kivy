from kivy.app import App
from kivy.uix.screenmanager import Screen


class Grupos(Screen):
    def on_enter(self, *args):
        print("Ingresando")
        App.get_running_app().ws.listar_grupos(_on_success=self.on_success_listar_grupos)

    def on_success_listar_grupos(self, req, result):
        print(result)




