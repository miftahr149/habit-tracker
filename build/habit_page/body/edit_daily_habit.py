import utility as util
import customtkinter as ctk
import tkinter as tk

from typing import Callable

from .daily_habit import CreateDailyHabit, DailyHabitProperty


class EditDailyHabit(CreateDailyHabit):

    def __init__(self, master: ctk.CTk, edit_command: Callable[[dict, dict], None],
                 delete_command: Callable,
                 daily_habit_data: tuple[str, dict[str, any]],
                 habit_property: list[dict[str, any]], **kwargs) -> None:

        super().__init__(
            master,
            create_command=edit_command,
            habit_property=habit_property
        )

        self.delete_command = delete_command
        self.edit_command = edit_command
        self.daily_habit_date, self.daily_habit_property = daily_habit_data

        self.build_configure()

    def build_configure(self) -> None:

        self.date.insert(0, self.daily_habit_date)
        self.property_configure()

        self.button.configure(
            text='Edit',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('edit_light'),
                dark_image=util.ImageStorage.get('edit_dark')
            ),
            command=util.Stack([
                lambda: self.edit_command(
                    {self.daily_habit_date: self.daily_habit_property},
                    self.get()
                ),
                self.destroy,
                lambda: util.VariableStorage.get('master') \
                    .winfo_children()[-1] \
                    .pack(expand=tk.YES, fill=tk.BOTH) 
            ])
        )

        self.delete_button = ctk.CTkButton(
            self.footer_frame,
            text='Delete', fg_color='red',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('trash_can_light'),
                dark_image=util.ImageStorage.get('trash_can_dark')
            ),
            command=util.Stack([
                self.delete_command,
                self.destroy,
                lambda: self.master.winfo_children()[-1] \
                    .pack(fill=tk.BOTH, expand=tk.YES)
            ])
        )
        self.delete_button.pack(fill=tk.X, padx=10, pady=10, side=tk.RIGHT)

    def property_configure(self) -> None:
        property_list: list[DailyHabitProperty]
        property_list = self.property_frame.winfo_children()

        property_value = list(self.daily_habit_property.values())

        for index, property_widget in enumerate(property_list):
            property_widget.sets(property_value[index])
