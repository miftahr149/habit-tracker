import utility as util
import customtkinter as ctk
import tkinter as tk

from typing import Callable

from .daily_habit import CreateDailyHabit


class EditDailyHabit(CreateDailyHabit):

    def __init__(self, master: ctk.CTk, edit_command: Callable[[dict, dict], None],
                 delete_command: Callable,
                 daily_habit_data: tuple[str, dict[str, any]], **kwargs) -> None:
        
        super().__init__(master, **kwargs)
        self.delete_command = delete_command
        self.edit_command = edit_command
        self.daily_habit_date, self.daily_habit_property = daily_habit_data

        self.build()
    
    def build(self) -> None:
        pass
