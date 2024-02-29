import tkinter as tk 
from tkinter import ttk 
from app.config import utils, color

"""
list_courses.py

This is the panel for the list of courses. The function of this panel is to
edit and remove the existing data from the course csv file.


"""

# list course box
class ListCoursesBox(tk.Listbox):
	def __init__(self, master):
		super().__init__(
			master=master,
			width=70,
			height=10,
			bg=color.BLUE,
			fg=color.PAPAYA
		)

		self.master = master
		self.bind("<<ListboxSelect>>", self.on_selection)

	def on_selection(self, event):
		selected = self.curselection()
		self.master.master.current_index = list(selected)[0]
		self.master.master.add_frame(list(selected)[0])

# the panel for the list courses button in the main app class.
class ListCourses(tk.Frame):
	def __init__(self, master):
		self.master = master
		super().__init__(
			master=master,
			bg=color.PEACH,
			width=600,
			height=500
		)
		self.master = master
		self.add_list_box()
		# self.add_frame()
		self.current_selected_data = False # this panel can only process one data at a time. 
		self.course_name = None 

	def add_labels(self): # add labels function, i basically divided all the children of this panel into functions, to make it more readable
		self.course_name_label = tk.Label(self.bottom_frame, text="Course Name:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.15, rely=0.3, anchor=tk.CENTER)
		self.course_id_label = tk.Label(self.bottom_frame, text="Course ID:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.17, rely=0.5, anchor=tk.CENTER)

	# adds a list box containing the latest data from the csv file.
	def add_list_box(self):
		self.top_frame = tk.Frame(self, width=560, height=230, bg=color.BLUE)
		self.top_frame.grid(row=0, column=0, padx=20, pady=20)
		self.top_frame.place()
		data = utils.course.read_all()
		if len(data):
			self.list_box = ListCoursesBox(self.top_frame)
			self.list_box.configure(justify=tk.CENTER)
			for idx, course in enumerate(data):
				self.list_box.insert(idx, course["name"])
			self.list_box.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		else:
			tk.Label(self.top_frame, bg=color.BLUE, fg=color.PAPAYA, text="No available Courses").place(relx=0.5, rely=0.5, anchor='center')


	def add_buttons(self):
		def done_button_callback():
			# delete the current row and add another
			edited_document = {
				"id": self.course_id.get("1.0", tk.END).strip("\n").replace(" ", "").upper(),
				"name": self.course_name.get("1.0", tk.END).strip("\n").title()
			}
			utils.course.edit_data(self.current_index, edited_document)

			self.course_name.config(state='disabled')
			self.course_id.config(state='disabled')
			self.edit_button.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
			self.done_button.place_forget()
			self.list_box.destroy()
			self.add_list_box()

		def edit_button_callback():
			self.course_name.config(state='normal')
			self.course_id.config(state='normal')
			self.edit_button.place_forget()
			self.done_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

		def delete_student():
			data = utils.course.fetch_one(self.current_index)
			utils.course.delete_one(data)
			self.list_box.destroy()
			self.add_list_box()
			self.confirmation_window.destroy()
			self.bottom_frame.destroy()

		def remove_button_callback():
			self.confirmation_window = tk.Toplevel(bg=color.BLUE)
			self.confirmation_window.title("Delete course?")
			self.confirmation_window.geometry("400x100")
			tk.Label(self.confirmation_window, text="Are you sure you want to delete these course?", bg=color.BLUE, fg='white').place(relx=0.5, rely=0.3, anchor=tk.CENTER)
			tk.Button(self.confirmation_window, text="Yes", width=5, command=delete_student, bg=color.BLUE, fg='white').place(relx=0.2, rely=0.7, anchor=tk.CENTER)
			tk.Button(self.confirmation_window, text="No", width=5, command=self.confirmation_window.destroy, bg=color.BLUE, fg='white').place(relx=0.8, rely=0.7, anchor=tk.CENTER)

		self.edit_button = tk.Button(self.bottom_frame, text="Edit", bg=color.BLUE, fg=color.PAPAYA, width=10, command=edit_button_callback)
		self.edit_button.place(relx=0.17, rely=0.8, anchor=tk.CENTER)
		self.done_button = tk.Button(self.bottom_frame, text="Done", bg=color.BLUE, fg=color.PAPAYA, width=10, command=done_button_callback)
		self.remove_button = tk.Button(self.bottom_frame, text="Remove", bg=color.BLUE, fg=color.PAPAYA, width=10, command=remove_button_callback)
		self.remove_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

	# the bottom frame consists of buttons and functions where the user can edit and remove course data.
	def add_frame(self, index):
		self.current_index = index

		self.bottom_frame = tk.Frame(self, width=560, height=210, bg=color.BLUE)
		if self.course_name is not None:
			self.course_name.destroy()
		self.course_name = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
		if not self.current_selected_data:
			self.bottom_frame.place_forget()
		
		self.bottom_frame.grid(row=1, column=0, padx=20, pady=0)
		self.bottom_frame.place()
		self.course_name.insert(tk.END, utils.course.fetch_one(index)["name"])
		self.course_name.config(state='disabled')
		self.course_name.place(relx=0.59, rely=0.3, anchor=tk.CENTER)
		
		self.course_id = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
		self.course_id.insert(tk.END, utils.course.fetch_one(index)["id"])
		self.course_id.config(state='disabled')
		self.course_id.place(relx=0.59, rely=0.5, anchor=tk.CENTER)
		self.current_selected_data = True
		self.add_labels()
		self.add_buttons()

