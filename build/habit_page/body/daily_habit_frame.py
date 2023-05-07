import utility as util
import tkinter as tk
import customtkinter as ctk


class DailyHabitFrame(ctk.CTkScrollableFrame):

    def __init__(self, master: ctk.CTkFrame, habit_data: dict, **kwargs) -> None:
        self.master = master
        super().__init__(self.master, **kwargs, fg_color='transparent')
        self.habit_data = habit_data
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
                lambda: print('Hello World')
            ])
        ).pack(fill=tk.X)
    
    def build_daily_habit(self) -> None:
        pass