import tkinter as tk
import customtkinter as ctk
import utility as util

from build import common

class Header(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, habit_name: str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.habit_name = habit_name
        self.build()

    def build(self) -> None:
        common.BackButton(
            self, 
            function=self.master.destroy
        ).pack(side=tk.LEFT, fill=tk.X, padx=(10, 0))

        ctk.CTkLabel(
            self,
            text=self.habit_name,
            font=('Helvetica', 16, 'bold')
        ).pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH, padx=(0, 10))