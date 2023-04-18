import tkinter as tk
import customtkinter as ctk


class OptionFrame(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        self.create_habit_button = ctk.CTkButton(self)
