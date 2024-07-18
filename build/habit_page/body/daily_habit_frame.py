import utility as util
import tkinter as tk
import customtkinter as ctk

from .daily_habit import CreateDailyHabit
from .edit_daily_habit import EditDailyHabit


class DailyHabitFrame(ctk.CTkScrollableFrame):

    def __init__(self, master: ctk.CTkFrame, habit_data: tuple[str, dict],  **kwargs) -> None:
        super().__init__(master, **kwargs, fg_color='transparent')
        self.habit_name, self.habit_property = habit_data
        self.daily_habit_storage: dict = util.JsonStorage\
            .get('habit', self.habit_name) \
            .get('daily_habit_list')
        self.build()

    def build(self) -> None:
        print(self.daily_habit_storage)

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
                    create_command=self.add_daily_habit,
                    habit_property=self.habit_property
                ).pack(expand=tk.YES, fill=tk.BOTH)
            ])
        ).pack(fill=tk.X)

    def build_daily_habit(self) -> None:
        
        def daily_habit_list(daily_habit_data: dict[str, dict]) -> ctk.CTkButton:
            daily_habit_date, daily_habit_value = daily_habit_data
            print(daily_habit_date)
            delete_command = lambda: self.delete_daily_habit(daily_habit_date)

            return ctk.CTkButton(
                self, 
                text=daily_habit_date,
                fg_color='transparent',
                command=util.Stack([
                    util.FunctionStorage.get('reset'),
                    lambda: EditDailyHabit(
                        util.VariableStorage.get('master'),
                        edit_command=self.edit_daily_habit,
                        daily_habit_data=daily_habit_data,
                        habit_property=self.habit_property,
                        delete_command=delete_command
                    ).pack(expand=tk.YES, fill=tk.BOTH)
                ])
            )

        for daily_habit_data in self.daily_habit_storage.items():
            daily_habit_list(daily_habit_data).pack(fill=tk.X)

    def add_daily_habit(self, daily_habit_data: dict) -> None:
        daily_habit_date, daily_habit_property = daily_habit_data.values()

        self.daily_habit_storage[daily_habit_date] = daily_habit_property
        util.JsonStorage.get('habit', self.habit_name).sets(
            'daily_habit_list', self.daily_habit_storage)

        util.reset_frame(self)
        self.build()

    def edit_daily_habit(self, old_habit_data, new_habit_data) -> None:
        old_habit_date = list(old_habit_data.keys())[0]
        del self.daily_habit_storage[old_habit_date]
        self.add_daily_habit(new_habit_data)
    
    def delete_daily_habit(self, daily_habit_date: str) -> None:
        print("Hello World")
        print(daily_habit_date)
        self.daily_habit_storage.pop(daily_habit_date)
        util.JsonStorage.get('habit', self.habit_name) \
            .sets('daily_habit_list', self.daily_habit_storage)
        for widget in self.winfo_children():
            widget.destroy()
        self.build()
        
