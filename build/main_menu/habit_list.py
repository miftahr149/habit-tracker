import tkinter as tk
import customtkinter as ctk
import utility as util

from build.habit_object import HabitObject


class HabitListFrame(ctk.CTkFrame):

    storage_habit: dict[util.OpenJson]

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.storage_habit = util.JsonStorage.load_from_folder('json')
        self.build()

    def build(self) -> None:
        for habit_name, habit_property in self.storage_habit.items():
            HabitObject(
                self,
                text=habit_name,
                fg_color='transparent',
                habit_property=habit_property,
            ).pack(fill=tk.X)

    def add_habit_function(self, habit: dict) -> None:
        habi_name, habit_property = habit.values()
        self.storage_habit[habit_name] = util.JsonStorage.create(habit_name)
        self.storage_habit[habit_name].sets('property', habit_property)
        util.reset_frame(self)
        self.build()
