import customtkinter as ctk
import tkinter as tk

class InputWidget(ctk.CTkFrame):

    def __init__(self, master: any, text: str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text=text).pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)