import tkinter as tk
import utility as util
import customtkinter as ctk
from typing import Callable

from .header import Header
from .body import Body
from .footer import Footer


class HabitPage(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk, habit_data: tuple[str, list[dict]], **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.habit_name, self.habit_property = habit_data
        self.build()

    def build(self) -> None:
        Header(self, self.habit_name).pack(fill=tk.X, ipady=10, pady=(0, 20))

        Body(
            self, 
            habit_data=(self.habit_name, self.habit_property)
        ).pack(expand=tk.YES, fill=tk.BOTH)

        # Footer()
