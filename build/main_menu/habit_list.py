import tkinter as tk
import customtkinter as ctk
import utility as util

from build.habit_page import HabitPage


class HabitListFrame(ctk.CTkFrame):

    storage_habit: dict[util.OpenJson]

    def __init__(self, master: any, **kwargs) -> None:
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
        util.JsonStorage.create('habit', habit_name).sets(
            'property', habit_property)
        self.storage_habit = util.JsonStorage.get('habit')
        util.reset_frame(self.habit_frame)
        self.add_habit_list()

    def add_habit_list(self) -> None:
        for habit_name, habit_property in self.storage_habit.items():
            ctk.CTkButton(
                self.habit_frame,
                text=habit_name,
                fg_color='transparent',
                command=util.Stack([
                    util.FunctionStorage.get('reset'),
                    lambda: HabitPage(
                        util.VariableStorage.get('master'),
                        habit_data=(habit_name, habit_property)
                    ).pack(expand=tk.YES, fill=tk.BOTH)
                ])
            ).pack(fill=tk.X, padx=10)
