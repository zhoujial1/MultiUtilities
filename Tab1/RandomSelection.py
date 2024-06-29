from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel

#import kv file
from kivy.lang import Builder
Builder.load_file('Tab1/RandomSelectionContent.kv')

class RandomSelectionContent(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
