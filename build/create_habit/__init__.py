import tkinter as tk
import customtkinter as ctk
from typing import Callable

import build.common as common
import utility as util

from .header import CreateHabitFrameHeader
from .body import CreateHabitFrameBody
from .foot import CreateHabitFrameFooter


class CreateHabitFrame(ctk.CTkFrame):

    def __init__(self, master: any, exit_func: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.exit_func = exit_func
        self.build()

    def build(self) -> None:
        pack_info = {
            'ipadx': 10,
            'ipady': 10
        }
        
        self.header = CreateHabitFrameHeader(self, fg_color='red', width=100)
        self.header.pack(**pack_info, fill=tk.X)

        self.body = CreateHabitFrameBody(self, fg_color='blue')
        self.body.pack(**pack_info, expand=tk.YES, fill=tk.BOTH)

        self.footer = CreateHabitFrameFooter(self, exit_func=self.exit_func, fg_color='green')
        self.footer.pack(**pack_info, fill=tk.X)
