import customtkinter as ctk
import tkinter as tk
import utility as util

from .habit_property import HabitProperty
from .input_widget import InputWidget


class Body(ctk.CTkScrollableFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        name_frame = InputWidget(self, text='Habit Name', fg_color='transparent')
        name_frame.pack(fill=tk.X, ipadx=10, ipady=10)

        self.name = ctk.CTkEntry(name_frame, width=200)
        self.name.pack(side=tk.LEFT)
        print(f'habit_name: {self.name.get()}')

        self.property = HabitProperty(self, fg_color='transparent')
        self.property.pack(expand=tk.YES, fill=tk.BOTH, pady=(10, 0))

    def get(self) -> dict:
        return {
            'name': self.name.get(),
            'property': self.property.get()
        }