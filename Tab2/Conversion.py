from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel

#Import kv file
from kivy.lang import Builder
Builder.load_file('Tab2/ConversionContent.kv')

class ConversionContent(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def convert_weight(self):
        # Conversion factors relative to kilogram
        conversion_factors = {
            'Tonne': 1000,
            'Kilogram': 1,
            'Gram': 0.001,
            'Miligram': 0.000001,
            'Microgram': 0.000000001,
            'Imperial Ton': 1016.0469088,
            'Stone': 6.35029318,
            'Pound': 0.45359237,
            'Ounce': 0.0283495231,
        }
        
        from_unit = self.ids.spinner_from.text
        to_unit = self.ids.spinner_to.text
        input_value = self.ids.input_from.text
        
        try:
            input_value = float(input_value)
        except ValueError:
            self.ids.input_to.text = 'Invalid input'
            return
        
        if from_unit in conversion_factors and to_unit in conversion_factors:
            value_in_kg = input_value * conversion_factors[from_unit]
            converted_value = value_in_kg / conversion_factors[to_unit]
            self.ids.input_to.text = str(converted_value)
        else:
            self.ids.input_to.text = 'Select valid units'

    def on_input_change(self, instance, value):
        # Call convert_weight whenever the input changes
        self.convert_weight()