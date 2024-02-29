import tkinter as tk  
from tkinter import ttk  
from app.frames import AddCourse, MainPanel, AddStudent, ListCourses, ListStudents

from app.config import utils, color

class LeftFrameButton(tk.Button):
	def __init__(self, master, text, width=20, command=None):
		super().__init__(
			master=master,
			text=text,
			width=width,
			height=1,
			bg=color.BLUE,
			fg=color.WHITE,
			font=("Default", 13),
			relief='groove',
			borderwidth=1,
			command=command
		)

class LeftFrame(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master=master,
			bg=color.BLUE,
			width=200,
			height=500
		)
		self.master = master
		# construct the message enum
		self.title()
		self.buttons()
		self.place_buttons()
		self.current_frame = None

	def title(self):
		title1 = tk.Label(self, text="Simple Student\nInformation System", fg=color.WHITE, bg=color.BLUE)
		title1.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

	def buttons(self):
		self.add_course = LeftFrameButton(self, text="Add Course", command=self.master.add_course_button)
		self.add_student = LeftFrameButton(self, text="Add Student", command=self.master.add_student_button)
		self.list_courses = LeftFrameButton(self, text="List Courses", command=self.master.list_courses_button)
		self.list_students = LeftFrameButton(self, text="List Students", command=self.master.list_students_button)
		self.quit_button = LeftFrameButton(
			self, 
			text="Quit",
			width="10",
			command=self.master.destroy
		)

	def place_buttons(self):
		self.add_course.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
		self.add_student.place(relx=0.5, rely=0.38, anchor=tk.CENTER)
		self.list_courses.place(relx=0.5, rely=0.46, anchor=tk.CENTER)
		self.list_students.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
		self.quit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)



class StudentSystem(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("800x500")
		self.resizable(False, False)
		self.configure(
			bg=color.PEACH
		)
		self.title("Simple Student Information System")

		self.left_panel = LeftFrame(self)
		self.left_panel.place(x=0, y=0)

		self.current_frame = None
		self.load_main_frame()

	def destroy_last_frame(self):
		if self.current_frame is None:
			return
		self.current_frame.destroy()

	def load_main_frame(self):
		self.destroy_last_frame()
		self.starter_panel = MainPanel(self)
		self.starter_panel.place(x=200, y=0)
		self.current_frame = self.starter_panel

	def add_course_button(self):
		self.destroy_last_frame()
		self.add_course_panel = AddCourse(self)
		self.add_course_panel.place(x=200, y=0)
		self.current_frame = self.add_course_panel

	def add_student_button(self):
		self.destroy_last_frame()
		self.add_student_panel = AddStudent(self)
		self.add_student_panel.place(x=200, y=0)
		self.current_frame = self.add_student_panel

	def list_courses_button(self):
		self.destroy_last_frame()
		self.list_courses_panel = ListCourses(self)
		self.list_courses_panel.place(x=200, y=0)
		self.current_frame = self.list_courses_panel

	def list_students_button(self):
		self.destroy_last_frame()
		self.list_students_panel = ListStudents(self)
		self.list_students_panel.place(x=200, y=0)
		self.current_frame = self.list_students_panel