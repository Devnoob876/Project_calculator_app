from kivy.app  import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



class Grid(GridLayout):
	def __init__(self, **kwargs):
		super(Grid, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text="lololo"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)
		




class The_app(App):
    def build(self):
    	return Grid()


if __name__ == "__main__":
    The_app().run()