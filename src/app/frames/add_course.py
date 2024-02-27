import tkinter as tk  
from app.config import color, utils

dash = "-" * 50

class AddCourse(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		self.course_id = None
		self.course_name = None
		self.course_description = None

		# ADD COURSE LABEL
		self.add_course_label = tk.Label(self, text="Add Course", 
									 	 font=('Default', 20), bg=color.PEACH, fg=color.CHARCOAL)
		self.add_course_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

		self.id_label = tk.Label(self, text="ID: ", font=('Default', 13), 
								 bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.3, rely=0.4, anchor=tk.CENTER)
		self.id_entry = tk.Entry(self, width=18, bg=color.PEACH, 
								 fg=color.CHARCOAL, font=('Default', 13))
		self.id_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

		self.name_label = tk.Label(self, text="Name:", font=('Default', 13), 
								   bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.265, rely=0.5, anchor=tk.CENTER)
		self.name_entry = tk.Entry(self, width=18, bg=color.PEACH, 
								   fg=color.CHARCOAL, font=('Default', 13))
		self.name_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.description_label = tk.Label(self, text="Description:", font=('Default', 13),
										  bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.224, rely=0.6, anchor=tk.CENTER)

		self.description_entry = tk.Entry(self, width=18, bg=color.PEACH,
										  fg=color.CHARCOAL, font=('Default', 13)
										  )
		self.description_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

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
		self.description_entry.delete(0, tk.END)