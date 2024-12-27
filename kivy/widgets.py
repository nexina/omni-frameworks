import os
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty

fonts_dir = os.path.join(os.path.dirname(__file__), 'fonts')

KIVY_FONTS = [
    {
        "name": "InriaSans",
        "fn_regular": os.path.join(fonts_dir, "InriaSans-Regular.ttf"),
        "fn_bold": os.path.join(fonts_dir, "InriaSans-Bold.ttf"),
        "fn_italic": os.path.join(fonts_dir, "InriaSans-Italic.ttf"),
        "fn_bolditalic": os.path.join(fonts_dir, "InriaSans-BoldItalic.ttf")
    }
]

for font in KIVY_FONTS:
    LabelBase.register(**font)


# Load the .kv file
Builder.load_file(os.path.join(os.path.dirname(__file__), 'widgets.kv'))

class OButton(Button):
    def __init__(self, **kwargs):
        super(OButton, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]

    b_color = ListProperty([0.133, 0.169, 0.169, 1])
    on_click_color = ListProperty([.4, .4, .4, 1])
    border_radius = ListProperty([8,])
    border_width = NumericProperty(0)
    border_color = ListProperty([1, 1, 1, 1])
    
    def update_text_color(self):
        if self.b_color[0] + self.b_color[1] >= 1 or self.b_color[0] + self.b_color[2] >= 1 or self.b_color[1] + self.b_color[2] >= 1:
            self.color = [0, 0, 0, 1]
        else:
            self.color = [1, 1, 1, 1]

    def on_b_color(self, instance, value):
        self.on_click_color = [value[0] + 0.3, value[1] + 0.3, value[2] + 0.3, 1]
        self.update_text_color()

class OTextField(TextInput):
    def __init__(self, **kwargs):
        super(OTextField, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]

    b_color = ListProperty([0.2, 0.2, 0.2, 1])
    border_radius = ListProperty([7,])
    border_width = NumericProperty(0)
    border_color = ListProperty([1, 1, 1, 1])
    foreground_color= ListProperty([1, 1, 1, 1])
    hint_color = ListProperty([1, 1, 1, 0.5])

    def update_hint_color(self, *args):
        r, g, b, a = self.foreground_color
        new_alpha = max(0, a - 0.2)
        self.hint_color = [r, g, b, new_alpha]

    
    def update_text_color(self):
        if self.b_color[0] + self.b_color[1] >= 1 or self.b_color[0] + self.b_color[2] >= 1 or self.b_color[1] + self.b_color[2] >= 1:
            self.color = [0, 0, 0, 1]
        else:
            self.color = [1, 1, 1, 1]

    def on_b_color(self, instance, value):
        self.update_text_color()


    pass

class OText(BoxLayout):
    text = StringProperty("New Text")
    color = ListProperty([1, 1, 1, 1])
    font_size = StringProperty("12sp")
    b_color = ListProperty([0, 0, 0, 0])
    
    def __init__(self, **kwargs):
        super(OText, self).__init__(**kwargs)

class OProgressBar(FloatLayout):
    max_value = NumericProperty(100)
    value = NumericProperty(0)
    b_color = ListProperty([0.2, 0.2, 0.2, 1])
    border_radius = ListProperty([7,])
    border_width = NumericProperty(0)
    border_color = ListProperty([1, 1, 1, 1])
    foreground_color = ListProperty([0.7, 0.7, 0.7, 1])
    color = ListProperty([1, 1, 1, 1])
    light_color = color
    dark_color = ListProperty([0.2, 0.2, 0.2, 1])
    font_size = StringProperty("15sp")

    def on_value(self, instance, value):
        self.update_text_color()
    

    def update_text_color(self):
        print("Value: ", self.value)
        if self.value / self.max_value >= 0.45:
            if self.foreground_color[0] + self.foreground_color[1] >= 1 or self.foreground_color[0] + self.foreground_color[2] >= 1 or self.foreground_color[1] + self.foreground_color[2] >= 1:
                self.color = self.dark_color
            else:
                self.color = self.light_color
        else:
            if self.b_color[0] + self.b_color[1] >= 1 or self.b_color[0] + self.b_color[2] >= 1 or self.b_color[1] + self.b_color[2] >= 1:
                self.color =  self.dark_color
            else:
                self.color = self.light_color
    pass

# class widgets(App):
#     def build(self):
#         gridLayout = GridLayout(cols=1)

#         button = OButton()
#         button.b_color = [1, 0, 0, 1]
#         # button.border_radius = [30,]
#         # button.border_width = 0
#         gridLayout.add_widget(button)

#         textfield = OTextField()
#         gridLayout.add_widget(textfield)

#         progressbar = OProgressBar()
#         gridLayout.add_widget(progressbar)
#         return gridLayout
    
# widgets()
# widgets().run()
