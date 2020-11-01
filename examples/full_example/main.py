from kivy.lang import Builder
from kivymd.app import MDApp

root_kv = """
#:import ExampleButton kivymd_extensions.example_extension.ExampleButton

BoxLayout:
    ExampleButton:
        text: "Click me!"
"""


class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()
