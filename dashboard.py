from kivy.app import App
from kivy.uix.screenmanager import Screen


class Dashboard(Screen):
    def on_enter(self, *largs):
        print("En grupo")
        self.grupo = App.get_running_app().store.get("current_grupo")["val"]
        self.ids["marca"].text = self.grupo["marca"]
        self.ids["potencia"].text = self.grupo["potencia"]
        self.ids["numero_de_serie"].text = self.grupo["numero_de_serie"]
        self.ids["modelo"].text = self.grupo["modelo"]

        App.get_running_app().set_informe_actual('')

        print(self.grupo)

    def volver(self):
        self.manager.current = 'grupos'

