import customtkinter as ctk
import tkinter as tk
import utility as util


class CreateHabitFrameBody(ctk.CTkScrollableFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        self.habit_name = HabitName(self)
        self.habit_name.pack(fill=tk.X)

        

    def get(self) -> dict:
        pass


class HabitName(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Name').pack(fill=tk.X, expand=tk.YES, side=tk.LEFT)
        self.habit_name = ctk.CTkEntry(self)
        self.habit_name.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    
    def get(self) -> str:
        return self.habit_name.get()
