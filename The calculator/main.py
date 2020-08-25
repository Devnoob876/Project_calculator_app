from kivy.app  import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import Builder


first_data = 0
second_data = 0
result = 0

class Mainscene(Screen):
    pass





class MyBox(GridLayout, Widget):

	def calculation(self, calculat):

		if calculat:
			try:
				self.display.text = str(eval(calculat))
			except Exception:
				self.display.text = "Error"
	


		








	




class thecalculator(App):
    def build(self):
    	return MyBox()



if __name__ == "__main__":
    sa = thecalculator()
    sa.run()
