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
        util.FunctionStorage.add([lambda: util.forget_all(self)], 'reset')
        util.ImageStorage.get_image_from_file('img')

        self.build()
        
    def build(self) -> None:
        pass
