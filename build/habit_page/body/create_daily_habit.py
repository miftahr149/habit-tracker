import utility as util
import customtkinter as ctk
import tkinter as tk
import datetime

from build import common
from typing import Callable


class CreateDailyHabit(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk, create_command: Callable, habit_property: dict, **kwargs) -> None:
        self.habit_property = habit_property
        self.create_command = create_command
        self.master = master
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))

        common.BackButton(
            self.header_frame,
            function=util.Stack([
                self.destroy,
                util.FunctionStorage.get('reset'),
                lambda: self.master.winfo_children(
                )[-1].pack(expand=tk.YES, fill=tk.BOTH)
            ])
        ).pack(side=tk.LEFT, padx=10, pady=10)

        self.body_frame = ctk.CTkFrame(self)
        self.body_frame.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.daily_habit_date = ctk.CTkEntry(
            self.body_frame,
            placeholder_text=self.get_today_date()
        )

    def get_today_date(self) -> str:
        today_date = datetime.datetime.now().date()
        return today_date.strftime("%d %B %Y")
