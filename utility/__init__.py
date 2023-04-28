import tkinter as tk
import customtkinter as ctk
from PIL import Image
import os
from typing import Callable

from .stack import Stack, FunctionStorage
from .image_storage import ImageStorage

def reset_frame(master: tk.Widget) -> None:
    for child in master.winfo_children():
        child.destroy()

def change_color(master:tk.Widget, color:str, master_change_color:bool=True) -> None:
    if master_change_color:
        try:
            master.configure(fg_color=color)
        except:
            return

    if isinstance(master, ctk.CTkFrame):
        for children in master.winfo_children():
            change_color(children, color)

def change_color_multiple(list_widget:list[tk.Widget], color:str) -> None:
    for widget in list_widget:
        change_color(widget, color)