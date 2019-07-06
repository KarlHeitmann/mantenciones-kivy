from kivy.uix.screenmanager import SlideTransition


def volver_trans(f):
    def func(self):
        print("Before calling")
        self.manager.transition = SlideTransition(direction="right")
        print("justo antes")
        f(self)
        print("After calling")

    return func


def siguiente_trans_tres(f):
    def func(self, req, result):
        print("Before calling")
        self.manager.transition = SlideTransition(direction="left")
        f(self, req, result)
        print("After calling")

    return func


def siguiente_trans(f):
    def func(*self):
        print("Before calling")
        self[0].manager.transition = SlideTransition(direction="left")
        f(*self)
        print("After calling")

    return func


def arriba_trans(f):
    def func(self):
        print("Before calling")
        self.manager.transition = SlideTransition(direction="down")
        f(self)
        print("After calling")
    return func


def abajo_trans(f):
    def func(self):
        print("Before calling")
        self.manager.transition = SlideTransition(direction="up")
        f(self)
        print("After calling")
    return func







