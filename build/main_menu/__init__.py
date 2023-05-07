import tkinter as tk
import customtkinter as ctk

import utility as util
from typing import Callable
from .habit_list import HabitListFrame
from .option import OptionFrame

class MainMenu(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()


    def build(self) -> None:
        self.habit_list = HabitListFrame(self)
        self.option = OptionFrame(self, create_command=self.habit_list.add_habit_function)

        self.option.pack(fill=tk.X, ipadx=30, ipady=30, pady=(0, 20))
        self.habit_list.pack(fill=tk.BOTH, expand=tk.YES)

        print(self.winfo_children())
