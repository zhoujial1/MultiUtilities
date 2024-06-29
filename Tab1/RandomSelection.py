import random
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

# Load the kv file
Builder.load_file('Tab1/RandomSelectionContent.kv')

class RandomSelectionContent(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_random_number(self):
        # Get the minimum and maximum values from the TextInput widgets
        min_value = self.ids.min_value.text
        max_value = self.ids.max_value.text

        # Convert the string values to integers
        try:
            min_value = int(min_value)
            max_value = int(max_value)
            if min_value > max_value:  # Ensure min_value is not greater than max_value
                self.ids.random_number.text = "Error: Min value is greater than Max value."
            else:
                # Generate a random number within the range
                random_number = random.randint(min_value, max_value)
                # Display the random number in the Label widget
                self.ids.random_number.text = "Your Number is: " + str(random_number)
        except ValueError:
            # Handle the case where the input is not a valid integer
            self.ids.random_number.text = "Please enter valid integers."