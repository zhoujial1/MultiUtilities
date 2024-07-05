from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('Tab3/TextUtilitiesContent.kv')

class TextUtilitiesContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_output(self, *args):
        text = self.ids.text_input.text
        # First role of options - Only one can be selected
        # If all_caps is selected, apply upper function to text
        if self.ids.all_caps.active:
            transformed_text = text.upper()
        # If all_lower is selected, apply lower function to text
        elif self.ids.all_lower.active:
            transformed_text = text.lower()
        # If title_case is selected, apply title function to text
        elif self.ids.title_case.active:
            transformed_text = text.title()
        # If swap_case is selected, apply swapcase function to text
        elif self.ids.swap_case.active:
            transformed_text = text.swapcase()
        # If no option is selected, transformed_text is the same as text
        else:
            transformed_text = text
        
        # Second role of options - Multiple can be applied
        # If reverse_text is selected, apply reverse_text function to text
        if self.ids.reverse_text.active:
            transformed_text = self.reverse_text(transformed_text, apply=False)
        # If strip_spaces is selected, apply strip_spaces function to text
        if self.ids.strip_spaces.active:
            transformed_text = self.strip_spaces(transformed_text, apply=False)
        # If strip_punctuation is selected, apply strip_special_chars function to text
        if self.ids.strip_punctuation.active:
            transformed_text = self.strip_special_chars(transformed_text, apply=False)
        # If strip_numbers is selected, apply strip_numbers function to text
        if self.ids.strip_numbers.active:
            transformed_text = self.strip_numbers(transformed_text, apply=False)
        
        # Update the output text after applying both roles of options
        self.ids.output.text = transformed_text
    
    # Function to reverse the text
    def reverse_text(self, text, apply=True):
        # Slicing the text with a step of -1 to reverse it
        result = text[::-1]
        # If apply is True, update the output text with the reversed text
        if apply:
            self.ids.output.text = result
        # If apply is False, return the reversed text
        else:
            return result
        
    # Function to remove spaces from the text
    def strip_spaces(self, text, apply=True):
        # Replace all spaces with an empty string
        result = text.replace(" ", "")
        # If apply is True, update the output text with the text without spaces
        if apply:
            self.ids.output.text = result
        # If apply is False, return the text without spaces
        else:
            return result
    
    # Function to remove special characters from the text
    def strip_special_chars(self, text, apply=True):
        # List of special characters
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # Join all characters that are not in the punctuation list
        no_punct = "".join(char for char in text if char not in punctuation)
        # If apply is True, update the output text with the text without special characters
        if apply:
            self.ids.output.text = no_punct
        # If apply is False, return the text without special characters
        else:
            return no_punct
        
    # Function to remove numbers from the text
    def strip_numbers(self, text, apply=True):
        # Join all characters that are not numbers
        no_numbers = ''.join(i for i in text if not i.isdigit())
        # If apply is True, update the output text with the text without numbers
        if apply:
            self.ids.output.text = no_numbers
        # If apply is False, return the text without numbers
        else:
            return no_numbers