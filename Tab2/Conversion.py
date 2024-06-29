from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel

#Import kv file
from kivy.lang import Builder
Builder.load_file('Tab2/ConversionContent.kv')

class ConversionContent(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)