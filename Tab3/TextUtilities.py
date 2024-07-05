from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('Tab3/TextUtilitiesContent.kv')

class TextUtilitiesContent(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_output(self, *args):
        text = self.ids.text_input.text
        if self.ids.all_caps.active:
            self.ids.output.text = text.upper()
        elif self.ids.all_lower.active:
            self.ids.output.text = text.lower()
        elif self.ids.title_case.active:
            self.ids.output.text = text.title()
        elif self.ids.swap_case.active:
            self.ids.output.text = text.swapcase()
        elif self.ids.reverse_text.active:
            self.reverse_text(text)
        elif self.ids.strip_spaces.active:
            self.strip_spaces(text)
        elif self.ids.strip_punctuation.active:
            self.strip_special_chars(text)
        elif self.ids.strip_numbers.active:
            self.strip_numbers(text)
        else:
            self.ids.output.text = text  # No transformation if no checkbox is selected
    
    def reverse_text(self,text):
        self.ids.output.text = text[::-1]
    
    def strip_spaces(self,text):
        self.ids.output.text = text.replace(" ", "")
    
    def strip_special_chars(self,text):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in text:
            if char not in punctuation:
                no_punct = no_punct + char
        self.ids.output.text = no_punct
        
    def strip_numbers(self,text):
        self.ids.output.text = ''.join([i for i in text if not i.isdigit()])