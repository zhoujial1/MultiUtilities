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
        
        # Get the incoming unit
        from_unit = self.ids.spinner_from.text
        # Get the outgoing unit
        to_unit = self.ids.spinner_to.text
        # Get the input value
        input_value = self.ids.input_from.text
        
        # Check if the input value is a number
        try:
            input_value = float(input_value)
        except ValueError:
            self.ids.input_to.text = 'Invalid input'
            return
        
        # Check if the incoming and outgoing units are in the conversion factors
        if from_unit in conversion_factors and to_unit in conversion_factors:
            # Convert the input value to kilogram
            value_in_kg = input_value * conversion_factors[from_unit]
            # Convert the kilogram value to the outgoing unit
            converted_value = value_in_kg / conversion_factors[to_unit]
            # Update the output text with the converted value
            self.ids.input_to.text = str(converted_value)
        # If the incoming or outgoing units are not in the conversion factors
        else:
            self.ids.input_to.text = 'Select valid units'

    def on_input_change(self, instance, value):
        # Call convert_weight whenever the input changes
        self.convert_weight()
    
    def convert_time(self):
        # Conversion factors relative to second
        conversion_factors = {
            'Second': 1,
            'Minute': 60,
            'Hour': 3600,
            'Day': 86400,
            'Week': 604800,
            'Month': 2628000,  # Approximation using 30.44 days per month
            'Year': 31536000,
        }

        # Get the incoming and outgoing units
        from_unit = self.ids.spinner_from_time.text
        to_unit = self.ids.spinner_to_time.text
        # Get the input value
        input_value = self.ids.input_from_time.text

        # Check if the input value is a number
        try:
            input_value = float(input_value)
        except ValueError:
            self.ids.input_to_time.text = 'Invalid input'
            return

        # Check if the incoming and outgoing units are in the conversion factors
        if from_unit in conversion_factors and to_unit in conversion_factors:
            # Convert the input value to seconds
            value_in_seconds = input_value * conversion_factors[from_unit]
            # Convert the seconds value to the outgoing unit
            converted_value = value_in_seconds / conversion_factors[to_unit]
            # Update the output text with the converted value
            self.ids.input_to_time.text = str(converted_value)
        else:
            self.ids.input_to_time.text = 'Select valid units'

    # Modify the on_input_change method to decide which conversion to use
    def on_input_change_time(self, instance, value):
        self.convert_time()