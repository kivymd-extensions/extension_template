from kivy.properties import BoundedNumericProperty
from kivymd.uix.button import MDRaisedButton


class ExampleButton(MDRaisedButton):
    width = BoundedNumericProperty(
        200, min=200, max=None, errorhandler=lambda x: 200
    )
