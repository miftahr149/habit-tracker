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
        self.daily_habit_data.pack(fill=tk.X, padx=10, pady=10)

        self.build_daily_habit_property()

    def build_daily_habit_property(self) -> None:
        for property_name, property_type in self.habit_property.items():
            property_frame = ctk.CTkFrame(self.body_frame)
            property_frame.pack(fill=tk.X, ipadx=10, ipady=10)

            ctk.CTkLabel(
                property_frame,
                text=property_name,
                anchor=tk.W
            ).pack(fill=tk.X, side=tk.LEFT)

            if habit_proeprty == "Chekclist":
                self.daily_habit_data[property_name] = ctk.BooleanVar(
                    value=False)
                ctk.CTkCheckBox(
                    property_frame, text='', width=200,
                    onvalue=True, offvalue=False,
                    variable=self.daily_habit_data[property_name],
                ).pack(side=tk.LEFT)

            if habit_property == 'Number':
                entry = ctk.CTkEntry(property_frame)
                entry.bind(
                    '<Key>',
                    lambda event: self.daily_habit_data.update(
                        {property_name: entry + event.char}
                    )
                )
                entry.pack(expand=tk.YES, fill=tk.BOTH)
