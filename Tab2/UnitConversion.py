from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class UnitConversionContent(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Welcome to Tab 2"))