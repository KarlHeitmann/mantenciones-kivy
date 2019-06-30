from kivy.uix.screenmanager import Screen


class Grupo(Screen):
    def on_enter(self, *largs):
        print(largs)
        print(*largs)
        indice = None
        if self.manager.screens[0].name == 'grupos':
            indice = 0
        elif self.manager.screens[1].name == 'grupos':
            indice = 1
        print("En grupo")


if __name__ == '__main__':
    pass
