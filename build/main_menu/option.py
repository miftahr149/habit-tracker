import tkinter as tk
import customtkinter as ctk
import utility as util
from build.create_habit import CreateHabitFrame
from typing import Callable

class OptionFrame(ctk.CTkFrame):

    def __init__(self, master: any, create_command: Callable, **kwargs) -> None:
        self.create_command = create_command
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        option_button_image = ctk.CTkImage(
            light_image=util.ImageStorage.get('plus_light'),
            dark_image=util.ImageStorage.get('plus_dark'))
        
        self.create_habit_button = ctk.CTkButton(self, 
            image=option_button_image, text='',
            command=util.Stack([
                util.FunctionStorage.get('reset'),
                lambda: CreateHabitFrame(
                    util.VariableStorage.get('master'),
                    command=self.create_command
                ).pack(expand=tk.YES, fill=tk.BOTH)
            ]),
            width=50, fg_color='transparent', border_width=0)
        self.create_habit_button.pack(side=tk.LEFT, padx=20)
