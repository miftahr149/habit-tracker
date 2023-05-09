import utility as util
import customtkinter as ctk
import tkinter as tk
import datetime

from build import common
from typing import Callable


class DailyHabit(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk, create_command: Callable, habit_property: dict, **kwargs) -> None:
        self.habit_property = habit_property
        self.create_command = create_command
        self.master = master
        super().__init__(master, **kwargs)

        self.daily_habit_data = dict()
        self.daily_habit_data['date'] = datetime.datetime.now().date()

        self.build()

    def build(self) -> None:
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))

        common.BackButton(
            self.header_frame,
            function=util.Stack([
                self.destroy,
                util.FunctionStorage.get('reset'),
                lambda: self.master.winfo_children(
                )[-1].pack(expand=tk.YES, fill=tk.BOTH)
            ])
        ).pack(side=tk.LEFT, padx=10, pady=10)

        self.body_frame = ctk.CTkFrame(self)
        self.body_frame.pack(expand=tk.YES, fill=tk.BOTH)

        self.daily_habit_date = ctk.CTkEntry(
            self.body_frame, border_width=0,
            font=('Helvetica', 20, 'bold'),
            placeholder_text=self.daily_habit_data.strftime("%d %B %Y"),
        )
        self.daily_habit_date.pack(fill=tk.X, padx=10, pady=10)

        self.build_daily_habit_property()

    def build_daily_habit_property(self) -> None:
        self.daily_habit_property_frame = ctk.CTkFrame(self.body_frame)
        for property_name, property_type in self.habit_property.items():
            create_widget = {
                'Number': lambda: DailyHabitPropertyNumber(
                    self.daily_habit_property_frame,
                    property_data=(property_name, property_type)
                ).pack(fill=tk.X),

                'Checklist': lambda: DailyHabitPropertyChecklist(
                    self.daily_habit_property_frame,
                    property_data=(property_name, property_type)
                ).pack(fill=tk.X),
            }

            create_widget[property_type]()


class DailyHabitProperty(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, **kwargs, fg_color='transparent')
        self.property_name = property_name
        self.variable = any()
        ctk.CTkLabel(self, text=self.property_name).pack(
            fill=tk.X, side=tk.LEFT)

    def get(self) -> any:
        return self.variable


class DailyHabitPropertyNumber(DailyHabitProperty):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, property_data, **kwargs)
        self.build()

    def build(self) -> None:
        self.number_entry = ctk.CTkEntry(self, width=200)
        self.number_entry.pack(side=tk.LEFT)

        self.number_entry('<FocusOut>', lambda event: self.set_variable())

    def set_variable(self) -> None:
        self.variable = int(self.number_entry.get())


class DailyHabitPropertyChecklist(DailyHabitProperty):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, property_data, **kwargs)
        self.build()

    def build(self) -> None:
        self.checklist = ctk.CTkCheckBox(
            self, text='',
            onvalue=True,
            offvalue=False,
            width=200
        )
        self.checklist.pack(side=tk.LEFT)

        self.number_entry('<FocusOut>', lambda event: self.set_variable())

    def set_variable(self) -> None:
        self.variable = self.checklist.get()
