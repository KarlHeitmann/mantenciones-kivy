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

TIPO_DE_PRUEBA = 'prueba_en_reposo'


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


class SelectableLabelInforme(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    primera_vez = True
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def btn_click(self):
        #print(self.ids["spinner_id"].text)
        print("clickeado")

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        if self.primera_vez:
            self.index = index
            print(data)
            self.ids["label_id"].text = ITEMS_PRUEBA_MANTENIMIENTO[TIPO_DE_PRUEBA][data['text']]["label"]
            tipo_de_dato = ITEMS_PRUEBA_MANTENIMIENTO[TIPO_DE_PRUEBA][data['text']]['tipo']
            self.input_text = None
            if isOption(tipo_de_dato):
                valores = tuple(TIPO_DE_DATO[tipo_de_dato])
                self.input_text = Spinner(values=valores)
                self.ids["box_layout_container"].add_widget(self.input_text)
            elif isInput(tipo_de_dato):
                self.input_text = TextInput()
                self.ids["box_layout_container"].add_widget(self.input_text)
            #self.ids["spinner_id"].values = ("uno", "dos", "tres", "cuatro")
            print(index)
            #return super(SelectableLabelInforme, self).refresh_view_attrs(
            #    rv, index, data)
            self.primera_vez = False

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
        #tipo_de_prueba = 'prueba_automatico'
        a = ITEMS_PRUEBA_MANTENIMIENTO[TIPO_DE_PRUEBA].keys()
        # elementos = [{ 'text': ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba][llave]["label"] } for llave in ITEMS_PRUEBA_MANTENIMIENTO[tipo_de_prueba].keys()]
        elementos = [{ 'text': llave } for llave in ITEMS_PRUEBA_MANTENIMIENTO[TIPO_DE_PRUEBA].keys()]

        self.ids["id_rv_informe"].inicializar(elementos)


