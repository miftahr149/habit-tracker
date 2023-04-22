import tkinter as tk
import customtkinter as ctk
import utility as util
from build.create_habit import CreateHabitFrame

class OptionFrame(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        self.create_habit_button = ctk.CTkButton(self, 
            image=util.get_image('img/Plus.ico'), text='',
            command=util.Stack([
                util.FunctionStorage.get('reset'),
                lambda: CreateHabitFrame(
                    util.FunctionStorage.get('get_master')(),
                    exit_func=util.Stack([
                        util.FunctionStorage.get('back_to_main')
                    ])
                ).pack(expand=tk.YES, fill=tk.BOTH)
            ]),
            width=50, fg_color='transparent', border_width=0)
        self.create_habit_button.pack(side=tk.LEFT, padx=20)
