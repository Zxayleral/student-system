import tkinter as tk 
from tkinter import ttk 

from app.config import utils, color


"""
add_student.py 
> this is the panel for the add course button. This is relatively the same with the add_course panel.
> some or all of the functions here are the same as the ones used in the add_course.py file.
"""

class AddStudent(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		self.current_notif = None
		# student label
		self.add_student_label = tk.Label(self, text="Add Student", font=('Default', 20), bg=color.PEACH, fg=color.CHARCOAL)
		self.add_student_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
		
		self.name_label = tk.Label(self, text="Name:", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.265, rely=0.4, anchor=tk.CENTER)
		self.name_entry = tk.Entry(self, width=18, bg=color.PEACH, fg=color.CHARCOAL, font=('Default', 13))
		self.name_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
		self.gender_label = tk.Label(self, text="Gender:", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.254, rely=0.5, anchor=tk.CENTER)
		self.gender_entry = ttk.Combobox(self, width=17, font=('Default', 13))
		self.gender_entry["values"] = ["Male", "Female", "LGBTQ+"] # these values are just suggestions.
		self.gender_entry.current()
		self.gender_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

		self.course_entry_label = tk.Label(self, text="Course: ", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.254, rely=0.6, anchor='center')
		self.course_entry = ttk.Combobox(self, width=17, font=("Default", 13))
		self.course_entry["values"] = [x["id"] for x in utils.course.read_all()]
		self.course_entry.current()
		self.course_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
		self.define_id_entry()

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
			text="ADD",
			width=7,
			height=1,
			font=('Default', 13),
			bg=color.PEACH,
			fg=color.CHARCOAL,
			command=self.add_button_callback
		).place(relx=0.8, rely=0.8, anchor=tk.CENTER)

	def define_id_entry(self):
		self.id_label = tk.Label(self, text="ID: ", font=('Default', 13), bg=color.PEACH, fg=color.CHARCOAL).place(relx=0.3, rely=0.3, anchor=tk.CENTER)
		self.id_entry = tk.Entry(self, width=18, bg=color.PEACH, fg=color.CHARCOAL, font=('Default', 13))
		self.id_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


	def success_notif(self):
		self.current_notif = tk.Label(self, text="Course has been successfully added!", font=('Default', 13), bg=color.PEACH, fg='black').place(relx=0.5, rely=0.9, anchor=tk.CENTER)

	def error_notif(self, message):
		if self.current_notif is not None:
			self.current_notif.destroy()
		self.current_notif = tk.Label(self, text=message, font=('Default', 13), bg=color.PEACH, fg='red').place(relx=0.5, rely=0.9, anchor=tk.CENTER)
	
	def validate_student(self, entry: dict):
		students = utils.student.read_all()
		if len(entry["id"]) > 9:
			self.error_notif("Your ID must only be 8 DIGITS.")	
			return False
		if not entry["id"].replace("-", "").isdigit():
			self.error_notif("Your ID must only contain DIGITS")	
			return False
		if entry["id"] in list(x["id"] for x in students):
			self.error_notif("The student ID matches one of the the existing records.")
			return False 
		if entry["name"] in list(x["name"] for x in students):
			self.error_notif("The student's name already exists.")
			return False
		return True

	def add_button_callback(self):
		entry = {
			"id": self.id_entry.get().strip().replace(" ", "").upper(),
			"name": self.name_entry.get().strip().title(),
			"gender": self.gender_entry.get().title(),
			"course": self.course_entry.get().strip().replace(" ", "").upper()
		}
		if not self.validate_student(entry):
			return

		utils.student.insert_one(entry)
		self.success_notif()
		self.clear_button_callback()
		

	def clear_button_callback(self):
		self.id_entry.delete(0, tk.END)
		self.name_entry.delete(0, tk.END)
		self.gender_entry.delete(0, tk.END)
		self.course_entry.delete(0, tk.END)