import customtkinter as ctk
import tkinter as tk
import utility as util
from typing import Callable


class CreateHabitFrameFooter(ctk.CTkFrame):

    def __init__(self, master: any, command: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.command = command
        self.build()

    def build(self) -> None:
        ctk.CTkButton(self, text='Create',
                      command=util.Stack([
                          util.FunctionStorage.get('back_to_main'),
                          self.command
                      ]), width=50).pack(expand=tk.YES, fill=tk.X, padx=10)
