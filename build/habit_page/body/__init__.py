import tkinter as tk
import customtkinter as ctk
import utility as util

from .daily_habit_frame import DailyHabitFrame


class Body(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, habit_data: tuple[str, list[dict]], **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.habit_name, self.habit_property = habit_data
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(
            self, text='Daily Habits', anchor=tk.W,
            font=('Helvetica', 16, 'bold')
        ).pack(fill=tk.X, padx=10, pady=10)

        self.daily_habit_frame = DailyHabitFrame(self, self.habit_property)
        self.daily_habit_frame.pack(expand=tk.YES, fill=tk.BOTH)

