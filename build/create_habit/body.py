import customtkinter as ctk
import tkinter as tk
import utility as util

from .add_property import WindowsAddProperty

class CreateHabitFrameBody(ctk.CTkScrollableFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        self.name = HabitName(self, fg_color='transparent')
        self.name.pack(fill=tk.X)

        self.property = HabitProperty(self, fg_color='transparent')
        self.property.pack(expand=tk.YES, fill=tk.BOTH, pady=(10, 0))

    def get(self) -> dict:
        pass


class HabitName(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Name').pack(fill=tk.X, expand=tk.YES, side=tk.LEFT)
        self.habit_name = ctk.CTkEntry(self, placeholder_text='Habits Name')
        self.habit_name.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
    
    def get(self) -> str:
        return self.habit_name.get()

class HabitProperty(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        image = ctk.CTkImage(
            light_image=util.ImageStorage.get('plus_light'),
            dark_image=util.ImageStorage.get('plus_dark'))

        self.add_property = ctk.CTkButton(
            self, image=image, text='Add Property',
            command=lambda: WindowsAddProperty(util.FunctionStorage.get('get_master')()),
            fg_color='transparent')
        self.add_property.pack(expand=tk.YES, fill=tk.X, side=tk.LEFT)