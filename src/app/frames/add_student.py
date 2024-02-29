import tkinter as tk 
from tkinter import ttk 

from app.config import utils, color


class AddStudent(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		# ADD COURSE LABEL
		self.add_course_label = tk.Label(self, text="Add Student", font=('Default', 20), bg=color.PEACH, fg=color.CHARCOAL)
		self.add_course_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
		self.id_label = tk.Label(self, text="ID: ", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.3, rely=0.4, anchor=tk.CENTER)
		self.id_entry = tk.Entry(self, width=18, bg=color.PEACH, fg=color.CHARCOAL, font=('Default', 13))
		self.id_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
		self.name_label = tk.Label(self, text="Name:", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.265, rely=0.3, anchor=tk.CENTER)
		self.name_entry = tk.Entry(self, width=18, bg=color.PEACH, fg=color.CHARCOAL, font=('Default', 13))
		self.name_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
		self.gender_label = tk.Label(self, text="Gender:", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.254, rely=0.5, anchor=tk.CENTER)
		self.gender_entry = ttk.Combobox(self, width=17, font=('Default', 13))
		self.gender_entry["values"] = [
			"Male", "Female", "Male (Born Female)", "Female (Born Male)",
			"Croissant", "Attack Helicopter", "Trans Racist", "Male (Born Alone)",
			"Female (Left by Dad)", "Non-Binary (Raised by Aliens)", "Male (Filipino)",
			"Female (Filipino)", "Female (Afam Enjoyer)", "Male (Alpha)", "Sigma", "Chill Bastard"
		]
		self.gender_entry.current()
		self.gender_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.course_entry_label = tk.Label(self, text="Course: ", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.)


		# buttons
		self.clear_button = tk.Button(
			self,
			text="CLEAR",
			width=7,
			height=1,
			font=('Default', 13),
			bg=color.PEACH,
			fg=color.CHARCOAL,
			command=self.clear_button_callback
		).place(relx=0.2, rely=0.8, anchor=tk.CENTER)

		self.add_button = tk.Button(
			self,
			text="NEXT",
			width=7,
			height=1,
			font=('Default', 13),
			bg=color.PEACH,
			fg=color.CHARCOAL,
			command=self.clear_button_callback
		).place(relx=0.8, rely=0.8, anchor=tk.CENTER)

	def add_button_callback(self):
		pass
		

	def clear_button_callback(self):
		self.id_entry.delete(0, tk.END)
		self.name_entry.delete(0, tk.END)
		self.gender_entry.delete(0, tk.END)