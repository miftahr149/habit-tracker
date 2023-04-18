import tkinter as tk
from PIL import ImageTk, Image
import os


def get_image(image_dir: str) -> ImageTk.PhotoImage:
    return ImageTk.PhotoImage(Image.open(image_dir))

def get_image_all(folder:str) -> dict[str, ImageTk.PhotoImage]:
    return {image.split('.')[0]:get_image(f'{folder}/{image}') for image in os.listdir(folder)}