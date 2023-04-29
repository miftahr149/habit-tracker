from customtkinter import CTkImage
from PIL import Image
import os


class ImageStorage:

    __container:dict[str, Image.open] = dict()

    @classmethod
    def get_image_from_file(cls, file:str) -> None:
        image_from_file = {image.split('.')[0]: Image.open(f'{file}/{image}') for image in os.listdir(file)}
        cls.__container.update(image_from_file)
    
    @classmethod
    def get(cls, name:str) -> Image.open:
        try:
            return cls.__container[name]
        except KeyError:
            print(f'there is no image call {name}')