import tkinter as tk 
from tkinter import LEFT, BOTTOM, TOP, RIGHT
from app.data import system

class LeftPanel(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master,
			width=200,
			height=460 - 30,
			borderwidth=2,
			relief='groove'
		)
		self.configure(
			background="#24273a"
		)
		self.pack(expand="yes")


class RightPanel(tk.Frame):
	def __init__(self, master):
		super().__init__(
			master
		)
		self.pack()
		self.set_canvas()
		self.scroll_bar()

	def set_canvas(self):
		self.canvas = tk.Canvas(self)
		self.canvas.pack(side=LEFT)
		self.canvas.configure(
			width=800 - 200 - 40 - 50,
			height=460 - 30 - 2,
			background="#24273a",
			borderwidth=2,
			relief='groove'
		)

	def scroll_bar(self):
		self.scroll_bar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
		self.scroll_bar.pack(side=RIGHT, fill='y')

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry("800x500")
		self.title("Student System")
		self.configure(background="#24273a")
		self.resizable(False, False)

		self.students = system.Students()

		self.menu()
		self.panel_shown = False
		self.info = None

	def menu(self):
		self.student_button = tk.Button(
			self, text="Students", bg= "#24273a",
			borderwidth=2,width=7,height=1,fg="#FFFFFF", command=self.toggle_panels
		)
		self.student_button.pack()
		self.student_button.place(x=20, y=10)

	def create_student_card(self):
		card = PaneWindow()
		return

	def student_manager(self):
		pass

	def toggle_panels(self):
		if not self.panel_shown:
			self.place_panels()
			self.panel_shown = True
		else:
			self.hide_panels()
			self.panel_shown = False

	def hide_panels(self):
		self.right_panel.place_forget()
		self.left_panel.place_forget()

	def place_panels(self):
		self.left_panel = LeftPanel(self)
		self.right_panel = RightPanel(self)

		self.right_panel.place(x=240, y=50)
		self.left_panel.place(x=20, y=50)

