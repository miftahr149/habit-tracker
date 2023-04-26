import tkinter as tk
import customtkinter as ctk
from .main_menu import MainMenu
import utility as util


class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.iconbitmap('favicon.ico')
        self.geometry('400x400')
        self.resizable(False, False)

        util.FunctionStorage([lambda: util.reset_frame(self)], 'reset')
        util.FunctionStorage([lambda: self], 'get_master')
        util.FunctionStorage([
            util.FunctionStorage.get('reset'),
            lambda: MainMenu(self).pack(expand=tk.YES, fill=tk.BOTH)
        ], 'back_to_main')
        util.ImageStorage.get_image_from_file('img')
        
        util.FunctionStorage.get('back_to_main')()