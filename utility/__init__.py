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