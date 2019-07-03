from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class LabelInfo(BoxLayout):
    label_string = StringProperty()

    def set_content(self, contenido):
        if contenido != None:
            self.ids["contenido_text"].text = contenido


