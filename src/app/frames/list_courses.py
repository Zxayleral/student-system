import tkinter as tk 
from tkinter import ttk 
from app.config import utils, color

class ListCoursesBox(tk.Listbox):
	def __init__(self, master):
		super().__init__(
			master=master,
			width=70,
			height=10,
			bg=color.CHARCOAL,
			fg=color.PAPAYA
		)

		self.master = master
		self.bind("<<ListboxSelect>>", self.on_selection)

	def on_selection(self, event):
		selected = self.curselection()
		self.master.add_frame(list(selected)[0])
		

class ListCourses(tk.Frame):
	def __init__(self, master):
		self.master = master
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		self.add_list_box()
		self.add_frame()
		self.current_selected_data = None

	def add_list_box(self):
		self.list_box = ListCoursesBox(self)
		self.list_box.configure(justify=tk.CENTER)
		data = utils.course.read_all()
		for idx, course in enumerate(data):
			self.list_box.insert(idx, course["name"])
		self.list_box.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

	def add_frame(self, index: int = None):
		frame = tk.Frame(self, width=460, height=230, bg = color.CHARCOAL)
		if index is None:
			frame.place(relx=0.5, rely=0.73, anchor=tk.CENTER)
		else:
			if self.current_selected_data is not None:
				self.current_selected_data.destroy()
			data = utils.course.read_all()
			id_label = tk.Label(self, text="ID: ", bg=color.CHARCOAL, fg=color.PAPAYA).place(relx=0.29, rely=0.6, anchor=tk.CENTER)
			
			id_entry = tk.Entry(self, bg=color.BLUE, fg=color.PAPAYA, width=37)
			id_entry.insert(0, data[index]["id"])
			id_entry.configure(state='disabled', justify=tk.CENTER)
			id_entry.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
			name_label = tk.Label(self, text="Name:", bg=color.CHARCOAL, fg=color.PAPAYA).place(relx=0.265, rely=0.67, anchor=tk.CENTER)
			name_entry = tk.Entry(self, bg=color.BLUE, fg=color.PAPAYA, width=37)
			name_entry.insert(0, data[index]["name"])
			name_entry.configure(state='disabled')
			name_entry.configure(justify=tk.CENTER)
			name_entry.place(relx=0.6, rely=0.67, anchor=tk.CENTER)

			description_label = tk.Label(self, text="Description: ", bg=color.CHARCOAL, fg=color.PAPAYA).place(relx=0.24, rely=0.74, anchor=tk.CENTER)
			description_entry = tk.Entry(self, bg=color.BLUE, fg=color.PAPAYA, width=37)
			description_entry.insert(0, data[index]["description"])
			description_entry.configure(state='disabled', justify=tk.CENTER)
			description_entry.place(relx=0.6, rely=0.74, anchor=tk.CENTER)