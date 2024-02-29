import tkinter as tk 
from tkinter import ttk 
from app.config import utils, color

"""
list_students.py

This file contains the panel class for the list students button in the left main panel.

All of the functions here are basically the same as the one used in the list courses panel.

"""

class ListStudentsBox(tk.Listbox):
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
        self.master.master.add_frame(list(selected)[0])

        

class ListStudents(tk.Frame):
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
        self.current_selected_data = False
        self.student_name = None

    def add_labels(self):
        self.student_id_label = tk.Label(self.bottom_frame, text="Student ID:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.17, rely=0.14, anchor=tk.CENTER)
        self.student_name_label = tk.Label(self.bottom_frame, text="Student Name:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.15, rely=0.27, anchor=tk.CENTER)
        self.student_gender_label = tk.Label(self.bottom_frame, text="Student Gender:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.15, rely=0.40, anchor=tk.CENTER)
        self.student_course_label = tk.Label(self.bottom_frame, text="Student Course:", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.15, rely=0.53, anchor=tk.CENTER)
        self.student_enrollement_label = tk.Label(self.bottom_frame, text="Student Status: ", bg=color.BLUE, fg=color.PAPAYA).place(relx=0.14, rely=0.66, anchor=tk.CENTER)

    def add_list_box(self):
        self.top_frame = tk.Frame(self, width=560, height=210, bg=color.BLUE)
        self.top_frame.grid(row=0, column=0, padx=20, pady=20)
        self.top_frame.place()
        data = utils.student.read_all()
        if len(data):
            self.list_box = ListStudentsBox(self.top_frame)
            self.list_box.configure(justify=tk.CENTER)
            for idx, student in enumerate(data):
                self.list_box.insert(idx, student["name"])
            self.list_box.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            tk.Label(self.top_frame, bg=color.BLUE, fg=color.PAPAYA, text="No available Students").place(relx=0.5, rely=0.5, anchor='center')

    def add_buttons(self):
        def done_button_callback():
            # delete the current row and add another
            edited_document = {
                "id": self.student_id.get("1.0", tk.END).strip("\n"),
                "name": self.student_name.get("1.0", tk.END).strip("\n"),
                "gender": self.student_gender.get("1.0", tk.END).strip("\n"),
                "course": self.student_course.get("1.0", tk.END).strip("\n")
            }
            utils.student.edit_data(self.current_index, edited_document)
            self.student_name.config(state='disabled')
            self.student_id.config(state='disabled')
            self.edit_button.place(relx=0.2, rely=0.85, anchor=tk.CENTER)
            self.done_button.place_forget()
            self.list_box.destroy()
            self.add_list_box()
            self.bottom_frame.destroy()
            self.add_frame(self.current_index)

        def edit_button_callback():
            self.student_name.config(state='normal')
            self.student_id.config(state='normal')
            self.student_gender.config(state='normal')
            self.student_course.config(state='normal')
            self.edit_button.place_forget()
            self.done_button.place(relx=0.8, rely=0.85, anchor=tk.CENTER)

        def delete_student():
            data = utils.student.fetch_one(self.current_index)
            utils.student.delete_one(data)
            self.list_box.destroy()
            self.add_list_box()
            self.confirmation_window.destroy()
            self.bottom_frame.destroy()

        def remove_button_callback():
            self.confirmation_window = tk.Toplevel(bg=color.BLUE)
            self.confirmation_window.title("Delete course?")
            self.confirmation_window.geometry("400x100")
            tk.Label(self.confirmation_window, text="Are you sure you want to delete these student?", bg=color.BLUE, fg='white').place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            tk.Button(self.confirmation_window, text="Yes", width=5, command=delete_student, bg=color.BLUE, fg='white').place(relx=0.2, rely=0.7, anchor=tk.CENTER)
            tk.Button(self.confirmation_window, text="No", width=5, command=self.confirmation_window.destroy, bg=color.BLUE, fg='white').place(relx=0.8, rely=0.7, anchor=tk.CENTER)
            

        self.edit_button = tk.Button(self.bottom_frame, text="Edit", bg=color.BLUE, fg=color.PAPAYA, width=10, command=edit_button_callback)
        self.edit_button.place(relx=0.17, rely=0.85, anchor=tk.CENTER)
        self.done_button = tk.Button(self.bottom_frame, text="Done", bg=color.BLUE, fg=color.PAPAYA, widt=10, command=done_button_callback)
        self.remove_button = tk.Button(self.bottom_frame, text="Remove", bg=color.BLUE, fg=color.PAPAYA, width=10, command=remove_button_callback)
        self.remove_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def enrollment_status(self):
        student = utils.student.fetch_one(self.current_index)
        courses = utils.course.read_all()
        if student["course"] in [x["id"].replace(" ", "") for x in courses]:
            return ["green", "enrolled"]
        else:
            return ["red", "not enrolled"]

    def add_frame(self, index):

        self.current_index = index

        self.bottom_frame = tk.Frame(self, width=560, height=230, bg=color.BLUE)
        if self.student_name is not None:
            self.student_name.destroy()
        self.student_name = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
        if not self.current_selected_data:
            self.bottom_frame.place_forget()
        
        self.bottom_frame.grid(row=1, column=0, padx=20, pady=0)
        self.bottom_frame.place()
        self.student_name.insert(tk.END, utils.student.fetch_one(index)["name"])
        self.student_name.config(state='disabled')
        self.student_name.place(relx=0.59, rely=0.27, anchor=tk.CENTER)
        
        self.student_id = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
        self.student_id.insert(tk.END, utils.student.fetch_one(index)["id"])
        self.student_id.config(state='disabled')
        self.student_id.place(relx=0.59, rely=0.14, anchor=tk.CENTER)
        

        self.student_gender = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
        self.student_gender.insert(tk.END, utils.student.fetch_one(index)["gender"])
        self.student_gender.config(state='disabled')
        self.student_gender.place(relx=0.59, rely=0.40, anchor=tk.CENTER)

        self.student_course = tk.Text(self.bottom_frame, bg=color.BLUE, borderwidth=2, fg=color.PAPAYA, height=1, width=45)
        self.student_course.insert(tk.END, utils.student.fetch_one(index)["course"])
        self.student_course.config(state='disabled')
        self.student_course.place(relx=0.59, rely=0.53, anchor=tk.CENTER)

        e_status = self.enrollment_status()
        self.student_enrollment_status = tk.Label(self.bottom_frame, bg=color.BLUE, fg=e_status[0], text=e_status[1].title()).place(relx=0.33, rely=0.66, anchor=tk.CENTER)

        self.current_selected_data = True
        self.add_labels()
        self.add_buttons()
