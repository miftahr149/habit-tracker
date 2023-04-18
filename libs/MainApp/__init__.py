import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.iconbitmap('favicon.ico')
        self.geometry('400x400')