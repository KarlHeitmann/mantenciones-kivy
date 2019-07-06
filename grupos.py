from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, SlideTransition

from decoradores import abajo_trans


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


        if not(index is None):
            if is_selected:
                print("buton pressed")
                print(index)
                id_grupo = rv.grupos[index]['id']
                print(id_grupo)
                App.get_running_app().set_grupo_actual(id_grupo)
                App.get_running_app().store.async_put(rv.callback_put_grupo, "current_grupo", val=rv.grupos[index])
                #mystore.get('plop', callback=my_callback)


        #rv.x = index
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
            rv.set_current(index)
        else:
            print("selection removed for {0}".format(rv.data[index]))



class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.__current = None

    def callback_put_grupo(self, arg1, arg2, arg3):
        #print(*kwargs)
        self.parent.parent.manager.current = 'dashboard'

    def inicializar(self, datos, grupos):
        self.grupos = grupos
        self.data=datos
        #self.grupos_id = grupos_id

    '''
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    '''

    def current(self):
        return self.__current

    def set_current(self, seleccion):
        self.__current = seleccion


class Grupos(Screen):
    def on_enter(self, *args):
        print("Ingresando")
        App.get_running_app().ws.listar_grupos(_on_success=self.on_success_listar_grupos, _on_failure=self.on_failure_listar_grupos)

    def on_failure_listar_grupos(self, req, result):
        if result['error'] == 'Not Authorized':
            self.cerrar_sesion()
            print('destruir')
            print(result)

    def on_success_listar_grupos(self, req, result):
        print(result)
        self.grupos_bruto = result
        #grupos = [{'text': fgrupo["marca"] + grupo["nombre_cliente"] + grupo["direccion"] + grupo["ciudad"]'} for grupo in result]
        grupos = [{'text': f'{grupo["marca"]} - {grupo["nombre_cliente"]} - {grupo["direccion"]} + {grupo["ciudad"]}'} for grupo in result]

        print(grupos)
        self.ids["id_rv"].inicializar(grupos, self.grupos_bruto)

    def btn_ver_on_press(self, index_data):
        if not(index_data is None):
            print("buton pressed")
            print(index_data)
            id_grupo = self.grupos_bruto[index_data]['id']
            print(id_grupo)
            App.get_running_app().store.async_put(self.callback_put_grupo, "current_grupo", val=self.grupos_bruto[index_data])
            #mystore.get('plop', callback=my_callback)

    def callback_put_grupo(self, arg1, arg2, arg3):
        #print(*kwargs)
        self.manager.current = 'grupo'

    @abajo_trans
    def goto_dashboard(self):
        # App.get_running_app().store.async_put(self.callback_put_grupo, "current_grupo", val=self.grupos_bruto[index_data])
        self.manager.current = 'dashboard'



