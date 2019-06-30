from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from eda_informes import ITEMS_PRUEBA_MANTENIMIENTO, TIPO_DE_DATO

def isInput(tipo):
    if ((tipo == 'voltaje') or (tipo == 'frecuencia') or (tipo == 'horas') or (tipo == 'temperatura_precision')):
        return True
    else:
        return False

def isArray(tipo):
    if (tipo == 'arreglo'): return True
    else: return False

def isOption(tipo):
    if ((tipo != 'voltaje') and (tipo != 'frecuencia') and (tipo != 'horas') and (tipo != 'temperatura_precision') and (tipo != 'arreglo')):
        return True;
    else:
        return False

class Informe(Screen):
    def on_enter(self):
        print("Ingresando")
        box_layout = BoxLayout(orientation="vertical")

        tipo_de_prueba = 'prueba_en_reposo'

        for linea in ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba].keys():
            lbl = Label(text=linea.replace('_', ' '))
            widget = None
            if isInput(ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][linea]["tipo"]):
                widget = TextInput()
            '''
            if not(widget is None):
                container = BoxLayout(orientation='vertical')
                container.add_widget(lbl)
                container.add_widget(widget)
            '''
            box_layout.add_widget(lbl)
        self.add_widget(box_layout)



