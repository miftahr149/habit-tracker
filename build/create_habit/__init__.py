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

        CreateHabitFrameHeader(self, width=100, fg_color='transparent').pack(
            **pack_info, fill=tk.X)

        self.body = CreateHabitFrameBody(self)
        self.body.pack(expand=tk.YES, fill=tk.BOTH)

        CreateHabitFrameFooter(self, exit_func=self.exit_func).pack(
            **pack_info, fill=tk.X)
