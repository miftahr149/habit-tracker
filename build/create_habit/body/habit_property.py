import tkinter as tk
import customtkinter as ctk
import utility as util
from typing import Callable

from .add_property import WindowsAddProperty
from .edit_property import WindowsEditProperty


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
                command=lambda habit_property: self.add_property_function(habit_property)),
            fg_color='transparent')
        self.add_property.pack(expand=tk.YES, fill=tk.X, side=tk.LEFT)

    def add_property_function(self, habit_property: dict) -> None:
        self.property_list.append(habit_property)
        util.reset_frame(self)
        self.build_property()

    def build_property(self) -> None:
        util.reset_frame(self)
        for habit_property in self.property_list:
            habit_property_frame = ctk.CTkFrame(self)
            habit_property_frame.pack(fill=tk.X)

            ctk.CTkButton(
                habit_property_frame,
                text=habit_property['name'],
                fg_color='transparent',
                command=lambda: WindowsEditProperty(
                    self,
                    command_edit=lambda old, new: self.edit_property_function(
                        old, new),
                    command_delete=util.Stack([
                        lambda: self.property_list.remove(habit_property),
                        self.build_property
                    ]),
                    habit_property=habit_property
                )
            ).pack(expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)

            ctk.CTkLabel(
                habit_property_frame,
                text=habit_property['type'],
                width=200
            ).pack(side=tk.LEFT)

            util.change_color(habit_property_frame, 'transparent')
        self.build()

    def edit_property_function(self, old: dict, new: dict) -> None:
        self.property_list[self.property_list.index(old)] = new
        self.build_property()
    
    def get(self) -> list[dict]:
        return self.property_list
