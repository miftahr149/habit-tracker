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
        self.title('Habit Tracker')

        util.VariableStorage.add('master', self)
        util.ImageStorage.get_image_from_file('img')

        util.FunctionStorage.add([
            lambda: util.check_visible_widget(self).pack_forget()
        ], 'reset')

        self.build()
        
    def build(self) -> None:
        main_menu = MainMenu(self)
        main_menu.pack(expand=tk.YES, fill=tk.BOTH)

        util.FunctionStorage.add([
            lambda: main_menu.pack(expand=tk.YES, fill=tk.BOTH)
        ], 'back_to_main')
