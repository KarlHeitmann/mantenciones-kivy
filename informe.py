from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from eda_informes import ITEMS_PRUEBA_MANTENIMIENTO, TIPO_DE_DATO



class Informe(Screen):
    def on_enter(self):
        print("Ingresando")
        box_layout = BoxLayout(orientation="vertical")
        for linea in ITEMS_PRUEBA_MANTENIMIENTO['prueba_en_reposo'].keys():
            lbl = Label(text=linea.replace('_', ' '))
            box_layout.add_widget(lbl)
        self.add_widget(box_layout)



