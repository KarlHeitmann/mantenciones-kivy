from kivy.app import App
from kivy.uix.screenmanager import Screen


class Mantenciones(Screen):
    pass


class MantencionesApp(App):
    def build(self):
        return Mantenciones()


if __name__ == '__main__':
    MantencionesApp().run()
