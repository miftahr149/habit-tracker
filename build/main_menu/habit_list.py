import tkinter as tk
import customtkinter as ctk
import utility as util

class HabitListFrame(ctk.CTkFrame):

    storage_habit:list[dict] = list()

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        for habit_data in self.storage_habit:
            print('hello world')
            

        self.label = ctk.CTkLabel(self, text='Habit List Section')
        self.label.pack(fill=tk.X, expand=tk.YES)
    
    def test_function(self, habit:dict) -> None:
        self.storage_habit.append(habit)
        util.reset_frame(self)
        self.build()