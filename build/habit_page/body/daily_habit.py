import utility as util
import customtkinter as ctk
import tkinter as tk
import datetime

from build import common
from typing import Callable


class CreateDailyHabit(ctk.CTkFrame):

    def __init__(self, master: ctk.CTk, create_command: Callable[[dict], None],
                 habit_property: list[dict[str, any]], **kwargs) -> None:
        self.habit_property = habit_property
        self.create_command = create_command
        self.master = master
        super().__init__(master, **kwargs)

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
                )[-1].pack(expand=tk.YES, fill=tk.BOTH),
            ])
        ).pack(side=tk.LEFT, padx=10, pady=10)

        self.body_frame = ctk.CTkFrame(self)
        self.body_frame.pack(expand=tk.YES, fill=tk.BOTH)

        today = datetime.datetime.now().date()

        self.date = ctk.CTkEntry(
            self.body_frame, border_width=0,
            fg_color='transparent',
            font=('Helvetica', 20, 'bold'),
            placeholder_text=today.strftime('%d %B %Y'),
        )
        self.date.pack(fill=tk.X, padx=10, pady=10)

        self.build_daily_habit_property()

        self.footer_frame = ctk.CTkFrame(self)
        self.footer_frame.pack(fill=tk.X)

        self.button = ctk.CTkButton(
            self.footer_frame,
            text='Create',
            image=ctk.CTkImage(
                light_image=util.ImageStorage.get('plus_light'),
                dark_image=util.ImageStorage.get('plus_dark')
            ),
            command=util.Stack([
                lambda: self.create_command(self.get()),
                self.destroy,
                lambda: self.master.winfo_children()[-1].pack(
                    expand=tk.YES, fill=tk.BOTH)
            ]),
        )
        self.button.pack(fill=tk.X, padx=10, pady=10, side=tk.LEFT)

    def get(self) -> dict:

        def get_property() -> dict[str, any]:
            habit_property_value: dict[str, any] = dict()
            property_list: list[DailyHabitProperty]

            property_list = self.property_frame.winfo_children()
            for widget in property_list:
                habit_property_value.update(widget.get())

            return habit_property_value

        def get_date() -> str:
            if self.date.get():
                return self.date.get()
            return datetime.datetime.now().strftime("%d %B %Y")

        return {
            'date': get_date(),
            'property': get_property()
        }

    def build_daily_habit_property(self) -> None:
        self.property_frame = ctk.CTkFrame(
            self.body_frame, fg_color='transparent')
        self.property_frame.pack(expand=tk.YES, fill=tk.BOTH)

        for property_data in self.habit_property:
            property_name, property_type = property_data.values()

            PACK_INFO = {
                'fill': tk.X,
                'padx': (20, 10)
            }

            create_widget = {
                'Number': lambda: DailyHabitPropertyNumber(
                    self.property_frame,
                    property_name=property_name
                ).pack(**PACK_INFO),

                'Checklist': lambda: DailyHabitPropertyChecklist(
                    self.property_frame,
                    property_name=property_name
                ).pack(**PACK_INFO),
            }

            create_widget[property_type]()


class DailyHabitProperty(ctk.CTkFrame):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, **kwargs, fg_color='transparent')
        self.property_name = property_name
        self.variable = None

        ctk.CTkLabel(
            self, text=self.property_name,
            font=('Helvetica', 16)
        ).pack(fill=tk.X, side=tk.LEFT)

    def get(self) -> dict[str, any]:
        return {self.property_name: self.variable}

    def get_property_name(self) -> str:
        return self.property_name

    def sets(self, value: any) -> None:
        self.variable = value


class DailyHabitPropertyNumber(DailyHabitProperty):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, property_name, **kwargs)
        self.build()

    def build(self) -> None:
        self.number_entry = ctk.CTkEntry(self, width=200)
        self.number_entry.pack(side=tk.LEFT)

        self.number_entry.bind('<FocusOut>', lambda event: self.set_variable())

    def set_variable(self) -> None:
        self.variable = int(self.number_entry.get())

    def sets(self, value: int) -> None:
        super().sets(value)
        self.number_entry.insert(0, str(value))


class DailyHabitPropertyChecklist(DailyHabitProperty):

    def __init__(self, master: ctk.CTkFrame, property_name: str, **kwargs) -> None:
        super().__init__(master, property_name, **kwargs)
        self.variable = False
        self.build()

    def build(self) -> None:
        self.checklist = ctk.CTkCheckBox(
            self, text='',
            onvalue=True,
            offvalue=False,
            fg_color='red',
            command=self.set_variable
        )
        self.checklist.pack(fill=tk.X, side=tk.RIGHT)

    def set_variable(self) -> None:
        self.variable = self.checklist.get()

    def sets(self, value: bool) -> None:
        super().sets(value)

        if value:
            return self.checklist.select()
        return self.checklist.deselect()
