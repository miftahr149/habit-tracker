import customtkinter as ctk
import tkinter as tk
import utility as util
from typing import Callable


class Footer(ctk.CTkFrame):

    def __init__(self, master: any, command: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.command = command
        self.build()

    def build(self) -> None:
        ctk.CTkButton(
            self, text='Create Habits',
            command=util.Stack([
                self.command,
                util.FunctionStorage.get('back_to_main')
            ]),
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('plus_light'),
                dark_image=util.ImageStorage.get('plus_dark')
            ), width=50
        ).pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
