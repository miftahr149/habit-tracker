import customtkinter as ctk
import tkinter as tk
import utility as util
from build import common

class Header(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Create New Habit', font=('Helvetica', 16, 'bold')).pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.RIGHT)
        common.BackButton(self, function=self.master.destroy).pack(side=tk.RIGHT, padx=10)
