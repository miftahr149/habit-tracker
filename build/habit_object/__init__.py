import tkinter as tk
import utility as util
import customtkinter as ctk


class HabitObject(ctk.CTkButton):

    def __init__(self, master: any, habit_data: dict, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.habit_data = habit_data
        self.build()
    
    def build(self) -> None:
        pass