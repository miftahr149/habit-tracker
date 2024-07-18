import tkinter as tk
import customtkinter as ctk
import utility as util

from build.habit_page import HabitPage


class HabitListFrame(ctk.CTkFrame):

    storage_habit: dict[util.OpenJson]

    def __init__(self, master: any, **kwargs) -> None:
        self.storage_habit: dict[str, util.OpenJson]
        
        super().__init__(master, **kwargs)
        self.storage_habit = util.JsonStorage.load_from_folder('habit')
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(
            self, text='List of your Habit: ', anchor=tk.W,
            font=('Helvetica', 16, 'bold')
        ).pack(fill=tk.X, padx=10, pady=10)

        self.habit_frame = ctk.CTkScrollableFrame(self, fg_color='transparent')
        self.habit_frame.pack(expand=tk.YES, fill=tk.BOTH)

        self.add_habit_list()

        if len(self.winfo_children()) == 0:
            ctk.CTkLabel(
                self,
                text="you haven't create any habit, go create one!"
            ).pack(expand=tk.YES, fill=tk.BOTH)

    def add_habit_function(self, habit: dict) -> None:
        habit_name, habit_property = habit.values()
        
        newHabitJson = util.JsonStorage.create('habit', habit_name)
        newHabitJson.sets('property', habit_property)
        newHabitJson.sets('daily_habit_list', {})

        self.storage_habit = util.JsonStorage.load_from_folder('habit')
        util.reset_frame(self.habit_frame)
        self.add_habit_list()

    def add_habit_list(self) -> None:
        for habit_name, habit_data in self.storage_habit.items():
            habit_property = habit_data.get('property')
            HabitObjectList(
                self.habit_frame,
                habit_data=(habit_name, habit_property)
            ).pack(fill=tk.X, padx=10)
            


class HabitObjectList(ctk.CTkButton):

    def __init__(self, master: ctk.CTkFrame, habit_data: tuple[str, list[dict]], **kwargs) -> None:
        self.habit_name, self.habit_property = habit_data
        super().__init__(
            master, text=self.habit_name,
            fg_color='transparent',
            command=util.Stack([
                util.FunctionStorage.get('reset'),
                lambda: HabitPage(
                    util.VariableStorage.get('master'),
                    habit_data=(self.habit_name, self.habit_property)
                ).pack(expand=tk.YES, fill=tk.BOTH)
            ])
        )