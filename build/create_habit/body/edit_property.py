import utility as util
import tkinter as tk
import customtkinter as ctk
from typing import Callable

from .add_property import WindowsAddProperty


class WindowsEditProperty(WindowsAddProperty):

    def __init__(self, master: any, command_edit: Callable,
                 command_delete: Callable, habit_property: dict, **kwargs) -> None:
        self.habit_property = habit_property
        self.command_delete = command_delete
        super().__init__(master, command_edit, **kwargs)
        self.title('Edit Property')
        self.test_function()

    def test_function(self) -> None:
        self.name.insert(0, self.habit_property['name'])

        self.type.set(self.habit_property['type'])
        self.type_function(self.type.get())

        if self.habit_property['type'] == 'Number':
            self.divide.delete(0, len(self.divide.get()))
            self.divide.insert(0, self.habit_property['setting']['divide'])

        self.delete_property_button = ctk.CTkButton(
            self.button_frame, text='Delete Property',
            command=util.Stack([
                self.destroy,
                self.command_delete
            ]), fg_color='red',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('trash_can_light'),
                dark_image=util.ImageStorage.get('trash_can_dark')
            )
        )
        self.delete_property_button.pack(
            fill=tk.X, side=tk.LEFT, padx=10, pady=10, expand=tk.YES)

        self.create_property_button.configure(
            text='Edit Property',
            command=util.Stack([
                lambda: self.command(self.habit_property, self.get_property()),
                self.destroy])
            )
