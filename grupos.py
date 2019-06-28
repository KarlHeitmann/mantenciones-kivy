from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        #self.data = [{'text': str(x)} for x in range(100)]
    def inicializar(self, datos):
        self.data=datos


class Grupos(Screen):
    def on_enter(self, *args):
        print("Ingresando")
        App.get_running_app().ws.listar_grupos(_on_success=self.on_success_listar_grupos)

    def on_success_listar_grupos(self, req, result):
        print(result)
        #grupos = [{'text': fgrupo["marca"] + grupo["nombre_cliente"] + grupo["direccion"] + grupo["ciudad"]'} for grupo in result]
        grupos = [{'text': f'{grupo["marca"]} - {grupo["nombre_cliente"]} - {grupo["direccion"]} + {grupo["ciudad"]}'} for grupo in result]
        print(grupos)
        self.ids["id_rv"].inicializar(grupos)




