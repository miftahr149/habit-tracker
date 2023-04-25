import customtkinter as ctk
import tkinter as tk
import utility as util
from typing import Callable

class BackButton(ctk.CTkButton):

    def __init__(self, master:any, function:Callable=None) -> None:
        command_function = util.FunctionStorage.get('back_to_main')
        if function:
            command_function = util.Stack([command_function, function])
        
        super().__init__(master, text='', 
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('back_light'),
                dark_image=util.ImageStorage.get('back_dark')),
            command=command_function, fg_color='transparent',
            border_width=0, width=30) 