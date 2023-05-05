import tkinter as tk
import utility as util
import customtkinter as ctk


class HabitObject(ctk.CTkButton):

    def __init__(self, master: any, habit_property: dict, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.habit_property = habit_property
        self.build()
    
    def build(self) -> None:
        pass