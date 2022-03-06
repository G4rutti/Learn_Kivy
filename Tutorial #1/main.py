import kivy
from kivy.app import App
from kivy.uix.label import Label

class RogerioApp(App):
    def build(self):
        return Label(text='Hello World', font_size=72)


if __name__ == '__main__':
    RogerioApp().run()