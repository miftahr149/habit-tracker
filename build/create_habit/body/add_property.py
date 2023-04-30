import tkinter as tk
import customtkinter as ctk
import utility as util
from typing import Callable


class InputWidget(ctk.CTkFrame):

    def __init__(self, master: any, text: str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text=text).pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)


class WindowsAddProperty(ctk.CTkToplevel):

    def __init__(self, master: any, command: Callable, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.command = command
        self.iconbitmap('favicon.ico')
        self.resizable(False, False)
        self.title('Add Property')
        self.build()

    def build(self) -> None:
        self.FRAME_PACK_INFO = {
            'fill': tk.X,
            'ipadx': 10,
            'ipady': 10
        }

        # Property Name
        self.name_frame = InputWidget(self, 'Property Name')
        self.name_frame.pack(**self.FRAME_PACK_INFO)

        self.name = ctk.CTkEntry(self.name_frame, width=200)
        self.name.pack(side=tk.LEFT)

        # Type of Property
        self.type_frame = InputWidget(self, 'Property Type')
        self.type_frame.pack(**self.FRAME_PACK_INFO)

        self.type = ctk.CTkOptionMenu(
            self.type_frame, width=200,
            values=['Checklist', 'Number'],
            command=self.type_function)
        self.type.pack(side=tk.LEFT)

        # Frame for Setting Property
        self.setting_property_frame = ctk.CTkFrame(self, height=0)
        self.setting_property_frame.pack(fill=tk.X, ipadx=10, ipady=10)

        # Create Property Button
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(side=tk.BOTTOM, **self.FRAME_PACK_INFO)

        self.create_property_button = ctk.CTkButton(
            self.button_frame, text='Create Property',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('plus_light'),
                dark_image=util.ImageStorage.get('plus_dark')
            ),
            command=util.Stack([
                lambda: self.command(self.get_property()),
                lambda: self.destroy()
            ])
        )
        self.create_property_button.pack(
            fill=tk.X, side=tk.LEFT, padx=10, pady=10, expand=tk.YES)

    def type_function(self, value) -> None:
        util.reset_frame(self.setting_property_frame)
        self.setting_property_frame.configure(height=0)

        if value == 'Number':
            self.divide_frame = InputWdiget('Divide by')
            self.divide_frame.pack(**self.FRAME_PACK_INFO)

            self.divide = ctk.CTkEntry(self.divide_frame, width=200)
            self.divide.pack(side=tk.LEFT)
            self.divide.insert(0, '100')
            
            return

    def get_property(self) -> dict:
        new_property = {
            'name': self.name.get() if self.name.get() != '' else self.type.get(),
            'type': self.type.get(),
        }

        if self.type.get() == 'Number':
            new_property['setting'] = {
                'divide': int(self.divide.get())
            }

        return new_property
