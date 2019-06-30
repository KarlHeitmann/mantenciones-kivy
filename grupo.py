from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class LabelInfo(BoxLayout):
    label_string = StringProperty()

    def set_content(self, contenido):
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

        print(self.grupo)


if __name__ == '__main__':
    pass
