import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

class MultiUtilitiesUI(TabbedPanel):
    pass

class MultiUtilities(App):
    def build(self):
        return MultiUtilitiesUI()
    
if __name__ == '__main__':
    MultiUtilities().run()