import tkinter as tk  
from app.config import color, utils

"""
starter.py

this file contains the main/starter panel of the GUI.

"""

class MainPanel(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		self.master = master
		self.add_course_label = tk.Label(
			self, 
			text="Hi! This is a Simple Student Information System\n"
				 "Feel free to access some features",
			bg=color.PEACH,
			fg=color.CHARCOAL,
			font=('Default', 15)
		)
		self.add_course_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)