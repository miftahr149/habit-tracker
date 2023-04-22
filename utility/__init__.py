import tkinter as tk
import customtkinter as ctk
from PIL import Image
import os
from typing import Callable

from .stack import Stack, FunctionStorage


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