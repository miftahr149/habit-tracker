import utility as util
import tkinter as tk
import customtkinter as ctk

from .create_daily_habit import CreateDailyHabit

class DailyHabitFrame(ctk.CTkScrollableFrame):

    def __init__(self, master: ctk.CTkFrame, habit_property: dict, **kwargs) -> None:
        super().__init__(master, **kwargs, fg_color='transparent')
        self.habit_property = habit_property
        self.build()

    def build(self) -> None:

        self.build_daily_habit()

        ctk.CTkButton(
            self, text='Create New',
            fg_color='transparent',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('plus_light'),
                dark_image=util.ImageStorage.get('plus_dark')
            ),
            command=util.Stack([
                util.FunctionStorage.get('reset'),
                lambda: CreateDailyHabit(
                    util.VariableStorage.get('master'),
                    create_command=self.add_daily_habit
                ).pack(expand=tk.YES, fill=tk.BOTH)
            ])
        ).pack(fill=tk.X)

    def build_daily_habit(self) -> None:
        pass
    
    def add_daily_habit(self, new_daily_habit: dict) -> None:
        pass
