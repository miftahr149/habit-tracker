import tkinter as tk
import customtkinter as ctk
from PIL import Image
import os
from typing import Callable


def get_image(image_dir: str | list[str, str], size: tuple = (20, 20)) -> ctk.CTkImage:
    print(f'dir: {image_dir}')
    light_image = image_dir
    dark_image = image_dir

    if image_dir == list:
        light_image, dark_image = image_dir

    return ctk.CTkImage(
        light_image=Image.open(light_image),
        dark_image=Image.open(dark_image),
        size=size)


def get_image_all(folder: str) -> dict[str, ctk.CTkImage]:
    return {image.split('.')[0]: get_image(f'{folder}/{image}') for image in os.listdir(folder)}


def reset_frame(master: tk.Widget) -> None:
    for child in master.winfo_children():
        child.destroy()


class Stack:

    stored_function = dict()

    def __init__(self, list_func: list[Callable], name: str = None) -> None:
        self.list_func = list_func
        if name: 
            self.list_func = self.stored_function[name] + self.list_func
    
    @classmethod
    def add_stored_function(cls, name: str, stored_function: list[Callable]) -> None:
        cls.stored_function[name] = stored_function

    def __call__(self) -> None:
        for func in self.list_func:
            func()
