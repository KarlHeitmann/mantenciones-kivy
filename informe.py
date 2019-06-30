from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from eda_informes import ITEMS_PRUEBA_MANTENIMIENTO, TIPO_DE_DATO
from grupos import SelectableLabel


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



class SelectableRecycleBoxLayoutInforme(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabelInforme(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabelInforme, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabelInforme, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''

        #rv.x = index
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
            rv.set_current(index)
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RVInforme(RecycleView):
    def __init__(self, **kwargs):
        super(RVInforme, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.__current = None

    def inicializar(self, datos):
        self.data=datos
        #self.grupos_id = grupos_id

    def current(self):
        return self.__current

    def set_current(self, seleccion):
        self.__current = seleccion



class Informe(Screen):
    def on_enter(self):
        print("Ingresando")
        box_layout1 = BoxLayout(orientation="vertical")
        box_layout2 = BoxLayout(orientation="vertical")
        #box_layout2 = BoxLayout(orientation="horizontal")

        tipo_de_prueba = 'prueba_en_reposo'
        #tipo_de_prueba = 'prueba_automatico'
        a = ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba].keys()
        elementos = [{ 'text': ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][llave]["label"] } for llave in ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba].keys()]

        self.ids["id_rv_informe"].inicializar(elementos)
        return
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

        #self.add_widget(box_layout1)
        #self.add_widget(box_layout2)



