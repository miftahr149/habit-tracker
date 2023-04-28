import tkinter as tk
import customtkinter as ctk
import utility as util


class WindowsAddProperty(ctk.CTkToplevel):

    def __init__(self, master: any, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.iconbitmap('favicon.ico')
        self.resizable(False, False)
        self.title('Add Property')
        self.build()

    def build(self) -> None:
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Property Name
        self.name_frame = ctk.CTkFrame(self.main_frame)
        self.name_frame.pack(fill=tk.X, ipadx=10, ipady=10)
        ctk.CTkLabel(self.name_frame, text='Property Name: ', justify=tk.LEFT).pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)
        self.name = ctk.CTkEntry(
            self.name_frame, placeholder_text='Property Name',
            width=200)
        self.name.pack(side=tk.LEFT)

        # Type of Property
        self.type_frame = ctk.CTkFrame(self.main_frame)
        self.type_frame.pack(fill=tk.X, ipadx=10, ipady=10)
        ctk.CTkLabel(self.type_frame, text='Property Type: ', justify=tk.LEFT).pack(
            expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)
        self.type = ctk.CTkOptionMenu(
            self.type_frame, width=200,
            values=['Checklist', 'Number'],
            command=self.type_function)
        self.type.pack(side=tk.LEFT)

        # Frame for Setting Property
        self.setting_property_frame = ctk.CTkFrame(self.main_frame)
        self.setting_property_frame.pack(fill=tk.X, ipadx=10, ipady=10)
        ctk.CTkLabel(self.setting_property_frame, text='').pack()

        # Create Property Button
        self.create_property_button = ctk.CTkButton(
            self.main_frame,
            image=ctk.CTkImage(light_image=util.ImageStorage.get('plus_light'),
                               dark_image=util.ImageStorage.get('plus_dark')),
            text='Create Property',
            command=lambda: self.button_function())
        self.create_property_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Change Color
        util.change_color_multiple([
            self.name_frame,
            self.type_frame,
            self.setting_property_frame
        ], 'transparent')

    def type_function(self, value) -> None:
        util.reset_frame(self.setting_property_frame)

        if value == 'Number':
            self.divide_frame = ctk.CTkFrame(
                self.setting_property_frame, fg_color='transparent')
            ctk.CTkLabel(self.divide_frame, text='Divide By: ', justify=tk.LEFT).pack(
                expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)
            self.divide = ctk.CTkEntry(self.divide_frame, width=200)
            self.divide.pack(side=tk.LEFT)
            self.divide.insert(0, '100')
            self.divide_frame.pack(fill=tk.X, ipadx=10, ipady=10)
            return
    
    def button_function(self) -> None:
        new_property = {
            'name':self.name.get(),
            'type':self.type.get()
        }
        util.FunctionStorage(lambda: new_property, 'new_habit_property')
        