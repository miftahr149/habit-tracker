import tkinter as tk
import customtkinter as ctk
import utility as util
from typing import Callable

from .add_property import WindowsAddProperty
from .edit_property import WindowsEditProperty
from .property_object import PropertyObject


class HabitProperty(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.property_list: list[dict] = list()
        self.build()

    def build(self) -> None:
        image = ctk.CTkImage(
            light_image=util.ImageStorage.get('plus_light'),
            dark_image=util.ImageStorage.get('plus_dark'))

        self.add_property = ctk.CTkButton(
            self, image=image, text='Add Property',
            command=lambda: WindowsAddProperty(
                self,
                command=self.add_property_function),
            fg_color='transparent')
        self.add_property.pack(expand=tk.YES, fill=tk.X, side=tk.LEFT)

    def add_property_function(self, habit_property: dict) -> None:
        self.property_list.append(habit_property)
        util.reset_frame(self)
        self.build_property()

    def build_property(self) -> None:
        util.reset_frame(self)
        for habit_property in self.property_list:
            PropertyObject(
                self, 
                _property=habit_property,
                command_edit=self.edit_property_function,
                command_delete=self.delete_property_function
            ).pack(fill=tk.X)
        self.build()

    def edit_property_function(self, old: dict, new: dict) -> None:
        self.property_list[self.property_list.index(old)] = new
        self.build_property()
    
    def delete_property_function(self, habit_property: dict) -> None:
        self.property_list.remove(habit_property)
        self.build_property()
    
    def get(self) -> list[dict]:
        return self.property_list
