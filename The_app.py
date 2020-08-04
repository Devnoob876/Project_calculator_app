from kivy.app  import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class The_app(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello kivy", font_size='20')
        sol = Label(text="Helo world")
        f.add_widget(s)
        s.add_widget(l)
        return f


if __name__ == "__main__":
    The_app().run()