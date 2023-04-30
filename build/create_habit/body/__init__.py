import customtkinter as ctk
import tkinter as tk
import utility as util

from .habit_property import HabitProperty


class Body(ctk.CTkScrollableFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        self.name = HabitName(self, fg_color='transparent')
        self.name.pack(fill=tk.X)

        self.property = HabitProperty(self, fg_color='transparent')
        self.property.pack(expand=tk.YES, fill=tk.BOTH, pady=(10, 0))

    def get(self) -> dict:
        pass


class HabitName(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.container = list()
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Name').pack(
            fill=tk.X, expand=tk.YES, side=tk.LEFT)
        self.habit_name = ctk.CTkEntry(
            self, placeholder_text='Habits Name', width=200)
        self.habit_name.pack(side=tk.LEFT)

    def get(self) -> str:
        return self.habit_name.get()