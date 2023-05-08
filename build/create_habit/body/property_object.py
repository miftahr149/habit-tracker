import customtkinter as ctk
import tkinter as tk
import utility as util

from typing import Callable
from .edit_property import WindowsEditProperty


class PropertyObject(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, _property: dict,
                 command_edit: Callable[[dict, dict], None], 
                 command_delete: Callable[[dict], None], 
                 **kwargs) -> None:

        super().__init__(master, **kwargs)
        self.property = _property
        self.command_edit = command_edit
        self.command_delete = command_delete
        self.build()

    def build(self) -> None:
        ctk.CTkButton(
            self,
            text=self.property['name'],
            fg_color='transparent',
            command=lambda: WindowsEditProperty(
                self, habit_property=self.property,
                command_edit=self.command_edit,
                command_delete=self.command_delete
            )
        ).pack(expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)

        ctk.CTkLabel(
            self, text=self.property['type'], 
            width=200
        ).pack(side=tk.LEFT)

        util.change_color(self, 'transparent')
