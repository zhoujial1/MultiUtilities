import random
import string
from datetime import datetime, timedelta
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

# Load the kv file
Builder.load_file('Tab1/RandomSelectionContent.kv')

class RandomSelectionContent(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    # Generate random number function
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
    
    # Shows slider number function for random letters
    def show_number(self, *args):
        # args[1] contains the new value of the slider
        slider_value = args[1]
        # Update the label's text with the new slider value, rounded to an integer
        self.ids.display_number.text = str(int(slider_value))
    # Generate random letters function
    def generate_letters(self):
        # Retrieve the number of letters to generate from the display_number label
        num_letters = int(self.ids.display_number.text)
        
        # Generate a random string of letters
        random_letters = ''.join(random.choices(string.ascii_letters, k=num_letters))
        
        # Display the generated string in the random_letters label
        self.ids.random_letters.text = "Your Letters: " + random_letters
    
    # Generate random date function 
    def generate_date(self):
        # Define the date range: last 10 years
        start_date = datetime.now() - timedelta(days=365 * 10)
        end_date = datetime.now()

        # Generate a random date within the range
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)

        # Format the date and display it
        self.ids.random_date.text = "Your Random Date: " + random_date.strftime('%Y-%m-%d')