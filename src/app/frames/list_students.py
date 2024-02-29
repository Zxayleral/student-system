import tkinter as tk
from tkinter import ttk 

from app.config import color, utils

class ListStudents(tk.Frame):
    def __init__(self, master):
        self.master = master 
        super().__init__(
            master=master,
            width=560,
            height=500,
            background=color.CHARCOAL
        )
        