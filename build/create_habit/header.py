import customtkinter as ctk
import tkinter as tk
import utility as util
from build import common

class CreateHabitFrameHeader(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Create Habit').pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.RIGHT)
        common.BackButton(self).pack(side=tk.RIGHT, padx=10)
