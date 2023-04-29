import customtkinter as ctk
import tkinter as tk
import utility as util

from .add_property import WindowsAddProperty
from .edit_property import WindowsEditProperty


class CreateHabitFrameBody(ctk.CTkScrollableFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.build()

    def build(self) -> None:
        self.name = HabitName(self, fg_color='transparent')
        self.name.pack(fill=tk.X)

        self.property = HabitProperty(self, fg_color='transparent')
        self.property.pack(expand=tk.YES, fill=tk.BOTH, pady=(10, 0))

    def get(self) -> dict:
        pass


class HabitName(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.container = list()
        self.build()

    def build(self) -> None:
        ctk.CTkLabel(self, text='Name').pack(
            fill=tk.X, expand=tk.YES, side=tk.LEFT)
        self.habit_name = ctk.CTkEntry(self, placeholder_text='Habits Name', width=200)
        self.habit_name.pack(side=tk.LEFT)

    def get(self) -> str:
        return self.habit_name.get()


class HabitProperty(ctk.CTkFrame):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.property_list: list[str, dict] = list()
        self.build()

    def build(self) -> None:
        image = ctk.CTkImage(
            light_image=util.ImageStorage.get('plus_light'),
            dark_image=util.ImageStorage.get('plus_dark'))

        self.add_property = ctk.CTkButton(
            self, image=image, text='Add Property',
            command=lambda: WindowsAddProperty(
                self, command=self.add_property_function),
            fg_color='transparent')
        self.add_property.pack(expand=tk.YES, fill=tk.X, side=tk.LEFT)

    def add_property_function(self) -> None:
        new_habit_property: dict = util.VariableStorage.get(
            'new_habit_property')
        self.property_list.append(new_habit_property)

        util.reset_frame(self)

        self.build_property()
        self.build()
    
    def build_property(self) -> None:
        for habit_property in self.property_list:
            habit_property_frame = ctk.CTkFrame(self)
            habit_property_frame.pack(fill=tk.X)

            ctk.CTkButton(
                habit_property_frame,
                text=habit_property['name'],
                fg_color='transparent',
                command=lambda: WindowsEditProperty(
                    self, command=lambda: self.edit_function(),
                    habit_property=habit_property
                )
            ).pack(expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)

            ctk.CTkLabel(
                habit_property_frame, 
                text=habit_property['type'],
                width=200
            ).pack(side=tk.LEFT)

            util.change_color(habit_property_frame, 'transparent')

    def edit_function(self) -> None:
        habit_property: dict = util.VariableStorage.get('new_habit_property')
        index = self.property_list.index(util.VariableStorage.get('old_habit_property'))
        self.property_list[index] = habit_property

        util.reset_frame(self)
        self.build_property()
        self.build()
    
    def delete_function(self) -> None:
        pass
        
