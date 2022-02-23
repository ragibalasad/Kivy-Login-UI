from kivy.config import Config

Config.set("graphics", "resizable", False)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.pickers import MDDatePicker


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class AwesomeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Red"

        return Builder.load_file("design.kv")

    def show_date_picker(self):
        date_dialogue = MDDatePicker(year=2004, month=8, day=2)
        date_dialogue.open()


if __name__ == "__main__":
    AwesomeApp().run()
