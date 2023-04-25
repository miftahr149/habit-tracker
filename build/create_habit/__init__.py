import tkinter as tk
import customtkinter as ctk
from typing import Callable
from .habit_option import HabitOptionFrame

import build.common as common
import utility as util

class CreateHabitFrame(ctk.CTkFrame):

    def __init__(self, master: any, exit_func: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.exit_func = exit_func
        self.build()
    
    def build(self) -> None:
        pack_info = {
            'ipadx':10,
            'ipady':10
        }
        CreateHabitFrameHeader(self, fg_color='red', width=100).pack(**pack_info, fill=tk.X)
        CreateHabitFrameBody(self, fg_color='blue').pack(**pack_info, expand=tk.YES, fill=tk.BOTH)
        CreateHabitFrameFooter(self, fg_color='green', width=100, exit_func=self.exit_func)\
            .pack(**pack_info, fill=tk.X)

class CreateHabitFrameHeader(ctk.CTkFrame):
    
    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        ctk.CTkLabel(self, text='Create Habit').pack(expand=tk.YES, fill=tk.BOTH, side=tk.RIGHT)
        common.BackButton(self).pack(side=tk.RIGHT, padx=10)

class CreateHabitFrameBody(ctk.CTkScrollableFrame):
    
    def __init__(self, master:any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()
    
    def build(self) -> None:
        pass

class CreateHabitFrameFooter(ctk.CTkFrame):
    
    def __init__(self, master:any, exit_func:Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.exit_func = exit_func
        self.build()
    
    def build(self) -> None:
        ctk.CTkButton(self, text='Create', 
            command=util.Stack([
                util.FunctionStorage.get('back_to_main'),
                self.exit_func
            ]), width=50).pack(expand=tk.YES, fill=tk.X, padx=10)