import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel

class MultiUtilitiesUI(TabbedPanel):
    pass

class MultiUtilities(App):
    def build(self):
        return MultiUtilitiesUI()
    
if __name__ == '__main__':
    MultiUtilities().run()