import tkinter as tk
import customtkinter as ctk
from typing import Callable

import build.common as common
import utility as util

from .header import Header
from .body import Body
from .footer import Footer



class CreateHabitFrame(ctk.CTkFrame):

    def __init__(self, master: any, command: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.command = command
        self.build()

    def build(self) -> None:
        PACK_INFO = {
            'ipadx': 10,
            'ipady': 10
        }

        Header(self, width=100, fg_color='transparent').pack(**PACK_INFO, fill=tk.X)

        self.body = Body(self)
        self.body.pack(expand=tk.YES, fill=tk.BOTH)

        Footer(
            self, 
            command=util.Stack([
                lambda: util.VariableStorage.add('habit_data', self.body.get()),
                util.FunctionStorage.get('back_to_main'),
                lambda: self.command(util.VariableStorage.get('habit_data'))
            ])
        ).pack(**PACK_INFO, fill=tk.X)
