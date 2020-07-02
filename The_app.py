import tkinter as tk
import tkinter.messagebox
import os
import datetime
import wikipedia
def exit_app():
	exit()

def back_farme_1():
	frame.pack()

def delete_frame():
	frame.pack_forget()
	
	frm1.pack()





	lbl1 = tk.Label(frm1, fg= "red",text="this is second frame if you click the button it will inform new frame", font=("Bold", 22))
	lbl1.pack()
	exbtn = tk.Button(frm1, fg="red", text="exit programm", font=("Italic"), command=exit_app)
	exbtn.pack()
	btn_back = tk.Button(frm1, fg="black", command=back_farme_1, font=("Roboto"), text="lol")
	btn_back.pack()



root = tk.Tk()
root.title("Learn pc")

frame = tk.Frame(root, width="2000", height= '2000')
frame.pack()
label = tk.Label(frame, fg= 'black',text="Learn your computer", font=("Italic", 22))
label.pack()

frm1 = tk.Frame(root,width="2000", height= '2000')
btn1 = tk.Button(frame, fg='red', font=("bold", 11), command=delete_frame, text="delete the text frame")
btn1.pack()


root.geometry('2000x2000')

root.mainloop()
#
##
###
####
#######
##########
################
#####################
########################
##############################
#################################
########################################
#########################################
####################################
###############################
#######################
###############
#########
######
####
###
##
#