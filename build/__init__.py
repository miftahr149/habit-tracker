import tkinter as tk
import customtkinter as ctk
from .main_menu import MainMenu

class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.iconbitmap('favicon.ico')
        self.geometry('400x400')
        self.build()
    
    def build(self) -> None:
        self.main_menu = MainMenu(self)
        self.main_menu.pack(expand=tk.YES, fill=tk.BOTH)