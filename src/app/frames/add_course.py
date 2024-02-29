import tkinter as tk  
from app.config import color, utils

"""
The code below is the code for the Add Course Panel. There are provided variable names that are easy to navigate.
"""

class AddCourse(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)


		self.add_course_label = tk.Label(self, text="Add Course", font=('Default', 20), bg=color.PEACH, fg=color.CHARCOAL)
		self.add_course_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


		self.id_label = tk.Label(self, text="ID: ", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.3, rely=0.4, anchor=tk.CENTER)
		

		self.id_entry = tk.Entry(self, width=18, bg=color.PEACH, fg=color.CHARCOAL, font=('Default', 13))
		self.id_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

		self.name_label = tk.Label(self, text="Name:", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.265, rely=0.5, anchor=tk.CENTER)
		self.name_entry = tk.Entry(self, width=18, bg=color.PEACH, 
								   fg=color.CHARCOAL, font=('Default', 13))
		self.name_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		# this is the current notif variable, it will be used for destroying current active labels[NOTIFICATIONS]
		self.current_notif = None

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
			text="ADD",
			width=7,
			height=1,
			font=('Default', 13),
			bg=color.PEACH,
			fg=color.CHARCOAL,
			command=self.add_button_callback
		).place(relx=0.8, rely=0.8, anchor=tk.CENTER)

	# a success notification
	def success_notif(self):
		self.success_label = tk.Label(self, text="Course has been uccessfully added", font=('Default', 13), bg=color.PEACH, fg='black').place(relx=0.5, rely=0.9, anchor=tk.CENTER)

	# a custom error message
	def error_notif(self, message):
		if self.current_notif is not None:
			self.current_notif.destroy()
		self.current_notif = tk.Label(self, text=message, font=('Default', 13), bg=color.PEACH, fg='red').place(relx=0.5, rely=0.9, anchor=tk.CENTER)
	
	# validator function for the given course entry.
	def validate_course(self, entry: dict):
		courses = utils.course.read_all() # reads all the courses from the csv file
		if entry["id"] in list(x["id"].replace(" ", "") for x in courses): # checks if the course already exists.
			self.error_notif("The course ID matches one of the the existing records.")
			return False 
		if entry["name"] in list(x["name"] for x in courses): # checks if the course name already exists
			self.error_notif("The course's name already exists.")
			return False
		return True

	def add_button_callback(self):
		entry = {
			"id": self.id_entry.get().strip().replace(" ", "").upper(),
			"name": self.name_entry.get().strip().title()
		}

		if not self.validate_course(entry): # check if the course if fully validated without any future errors
			return

		utils.course.insert_one(entry)
		self.success_notif() # adds a successful notification
		self.clear_button_callback() 

	# clears all the entries given by the user in the panel
	def clear_button_callback(self):
		self.id_entry.delete(0, tk.END)
		self.name_entry.delete(0, tk.END)