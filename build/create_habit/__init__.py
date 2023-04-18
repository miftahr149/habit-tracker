import tkinter as tk
import customtkinter as ctk
from typing import Callable
from .habit_option import HabitOptionFrame

class CreateHabitFrame(ctk.CTkFrame):

    def __init__(self, master: any, exit_func: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.exit_func = exit_func
        self.build()
    
    def build(self) -> None:
        label = ctk.CTkLabel(self, text='Create Habit View')
        label.pack(expand=tk.YES)

        self.habit_option = HabitOptionFrame()

        self.exit_button = ctk.CTkButton(self, command=self.exit_func)