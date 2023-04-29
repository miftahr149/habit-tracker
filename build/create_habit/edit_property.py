import utility as util
import tkinter as tk
import customtkinter as ctk
from typing import Callable

from .add_property import WindowsAddProperty


class WindowsEditProperty(WindowsAddProperty):

    def __init__(self, master: any, command: Callable, habit_property: dict, **kwargs) -> None:
        self.habit_property = habit_property
        util.VariableStorage.add('old_habit_property', self.habit_property)
        super().__init__(master, command, **kwargs)
        self.title('Edit Property')
        self.test_function()
    
    def test_function(self) -> None:
        self.name.insert(0, self.habit_property['name'])
        
        self.type.set(self.habit_property['type'])
        self.type_function(self.type.get())
        if self.habit_property['type'] == 'Number':
            self.divide.delete(0, len(self.divide.get()))
            print(self.divide.get())
            self.divide.insert(0, self.habit_property['setting']['divide'])

        self.delete_property_button = ctk.CTkButton(
            self.button_frame, text='Delete Property',
            command=util.Stack([
                
            ]), fg_color='red'
        )
        self.create_property_button.configure(text='Edit Property')