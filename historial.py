from kivy.app import App
from kivy.uix.screenmanager import Screen

from decoradores import arriba_trans


class Historial(Screen):
    def on_enter(self):
        self.index = 1
        self.grupo = App.get_running_app().get_grupo_actual()
        App.get_running_app().ws.buscar_maintenance(self.grupo["id"], self.index, _on_success=self.callback_historial_success)

    def btn_siguiente(self):
        self.index = self.index - 1 if self.index > 1 else 0
        print(self.index)
        App.get_running_app().ws.buscar_maintenance(self.grupo["id"], self.index, _on_success=self.callback_historial_success)

    def btn_anterior(self):
        self.index = self.index + 0 if self.grupo is None else 1
        print(self.index)
        App.get_running_app().ws.buscar_maintenance(self.grupo["id"], self.index, _on_success=self.callback_historial_success)

    def callback_historial_success(self, req, result):
        print(result)
        if result['maintenance'] is None:
            self.ids["label_maintenance"].text = "[b]No[/b]"
            self.ids["lbl_actual"].text = "1"
        else:
            self.mantencion = result['maintenance']
            self.ids["lbl_actual"].text = "%s:\nFecha: %s" %(self.index, self.mantencion["created_at"])
            texto = ""
            # for key, value in result['maintenance']:
            for key in self.mantencion:
                if (key == "_id") or (key == 'created_at') or (key == 'electric_generator_id') or (key == 'image_uid'):
                    pass
                else:
                    if isinstance(self.mantencion[key], dict):
                        texto = texto + '\n[b]' + str(key) + '[/b]' + '\n'
                        for key_2 in self.mantencion[key]:
                            if self.mantencion[key][key_2] is None:
                                pass
                            else:
                                texto = texto + str(key_2) + ': ' + self.mantencion[key][key_2] + '\n'
                    else:
                        texto = texto + str(key)  + ": " + str(self.mantencion[key]) + '\n'
            self.ids["label_maintenance"].text = texto

    @arriba_trans
    def volver(self):
        self.manager.current = 'dashboard'