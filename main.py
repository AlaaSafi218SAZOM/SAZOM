from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from server import SERVER
import subprocess
import os
SAZOMF = "./SAZOM_A-Z/"
if os.path.exists(SAZOMF):
    print("alredy - [SAZOM_A-Z]")
    pass
else:
    os.makedirs("SAZOM_A-Z")
    print("creat folder - [SAZOM_A-Z]")
SERVER()
class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.command_label = Label(text="Commands:")
        self.command_output = Label(text="", size_hint_y=0.8)
        self.start_button = Button(text="Start SAZOM", on_press=self.start_action)
        self.stop_button = Button(text="Stop SAZOM", on_press=self.stop_action)

        self.add_widget(self.command_label)
        self.add_widget(self.command_output)
        self.add_widget(self.start_button)
        self.add_widget(self.stop_button)

    def start_action(self, instance):
        print("Start SAZOM button pressed")
        self.start_button.background_color = (0, 1, 0, 1)  # Green color
        self.stop_button.background_color = (1, 0, 0, 1)    # Red color
        self.command_output.text += f"Start SAZOM command executed\n"
        
        # Add your code to start execution here
        subprocess.Popen(["python", "./SAZOM_A-Z/SAZOM.py"])

    def stop_action(self, instance):
        print("Stop SAZOM button pressed")
        self.start_button.background_color = (1, 0, 0, 1)    # Red color
        self.stop_button.background_color = (0, 1, 0, 1)  # Green color
        self.command_output.text += "Stop SAZOM command executed\n"
        subprocess.stop_code(["python", "./SAZOM_A-Z/SAZOM.py"])
        # Add your code to stop execution here

class SAZOM(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    SAZOM().run()

