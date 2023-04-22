import tkinter as tk
import customtkinter as ctk

import utility as util
from typing import Callable
from .habit_list import HabitListFrame
from .option import OptionFrame

class MainMenu(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        #print('Hello World')
        self.build()


    def build(self) -> None:
        self.option = OptionFrame(self, fg_color='red')
        self.option.pack(fill=tk.X, ipadx=30, ipady=30, pady=(0, 10))

        self.habit_list = HabitListFrame(self, fg_color='blue')
        self.habit_list.pack(fill=tk.BOTH, expand=tk.YES)
