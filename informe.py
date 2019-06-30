from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from eda_informes import ITEMS_PRUEBA_MANTENIMIENTO, TIPO_DE_DATO


def isInput(tipo):
    if ((tipo == 'voltaje') or (tipo == 'frecuencia') or (tipo == 'horas') or (tipo == 'temperatura_precision')):
        print(tipo)
        return True
    else:
        print(tipo)
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
        box_layout1 = BoxLayout(orientation="vertical")
        box_layout2 = BoxLayout(orientation="vertical")
        #box_layout2 = BoxLayout(orientation="horizontal")

        tipo_de_prueba = 'prueba_en_reposo'
        #tipo_de_prueba = 'prueba_automatico'

        i = 0

        for linea in ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba].keys():
            widget = None
            #if isInput(ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][linea]["tipo"]):
            #    widget = TextInput()
            if isOption(ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][linea]["tipo"]):
                print(tuple(TIPO_DE_DATO[ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][linea]["tipo"]]))
                widget = Spinner(
                    # default value shown
                    text='',
                    # available values
                    #values=('Home', 'Work', 'Other', 'Custom'),
                    values = tuple(TIPO_DE_DATO[ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][linea]["tipo"]]),
                    # just for positioning in our example
                    #size_hint=(None, None),
                    #size=(100, 44),
                    #pos_hint={'center_x': .5, 'center_y': .5}
                )
            if not(widget is None):
                lbl = Label(text=linea.replace('_', ' '))
                container = BoxLayout(orientation='horizontal')
                container.add_widget(lbl)
                container.add_widget(widget)
                if i < 10:
                    box_layout1.add_widget(container)
                #elif i < 20:
                #    box_layout1.add_widget(container)
                #else:
                #    box_layout2.add_widget(container)
            else:
                lbl = Label(text=linea.replace('_', ' '))
                if i < 10:
                    box_layout1.add_widget(lbl)
                #elif i < 20:
                #    box_layout1.add_widget(lbl)
                #else:
                #    box_layout2.add_widget(lbl)
            i += 1

        self.add_widget(box_layout1)
        #self.add_widget(box_layout2)



