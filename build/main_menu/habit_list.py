import tkinter as tk
import customtkinter as ctk
import utility as util

from build.habit_object import HabitObject

class HabitListFrame(ctk.CTkFrame):

    storage_habit:dict[str, util.OpenJson] = dict()

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        for habit_data in self.storage_habit:
            HabitObject(
                self,
                habit_data=habit_data,
            ).pack(expand=tk.YES, ipadx=10, ipady=10)
    
    def add_habit_function(self, habit:dict) -> None:
        self.storage_habit[habit['name']] = util.JsonStorage.create(habit['name'])
        self.storage_habit[habit['name']].sets('property', habit[])
        util.reset_frame(self)
        self.build()