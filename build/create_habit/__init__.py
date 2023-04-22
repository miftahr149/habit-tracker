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

        button = ctk.CTkButton(self, text='Click Me', command=self.exit_func)
        button.pack(expand=tk.YES)

class CreateHabitFrameHeader(ctk.CTkFrame):
    
    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build() -> None:
        self.label = ctk.CTkLabel(self, text='Create Habit')
        self.label.pack(expand=tk.YES, fill=tk.BOTH)