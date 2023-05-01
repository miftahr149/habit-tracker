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

        util.FunctionStorage.add([lambda: util.reset_frame(self)], 'reset')
        util.FunctionStorage.add([
            util.FunctionStorage.get('reset'),
            lambda: MainMenu(self).pack(expand=tk.YES, fill=tk.BOTH)
        ], 'back_to_main')

        

        util.ImageStorage.get_image_from_file('img')
        
        util.FunctionStorage.execute('back_to_main')