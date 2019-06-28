from kivy.app import App

from login import Login


class MantencionesApp(App):
    def build(self):
        return Login()


if __name__ == '__main__':
    MantencionesApp().run()
