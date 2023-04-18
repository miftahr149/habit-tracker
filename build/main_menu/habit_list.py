import tkinter as tk
import customtkinter as ctk


class HabitListFrame(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        self.label = ctk.CTkLabel(self, text='Habit List Section')
        self.label.pack(fill=tk.X, expand=tk.YES)