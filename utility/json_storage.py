import json
import os

from typing import Any

class OpenJson:

    def __init__(self, folder_name: str, file_name: str) -> None:
        self.file_dir = f'json/{folder_name}/{file_name}.json'

        if not os.path.exists(self.file_dir):
            open(self.file_dir, 'a').close()

        with open(self.file_dir, 'r+') as file:
            self.storage = dict()
            if os.path.getsize(self.file_dir) > 0:
                self.storage = json.loads(file.read())

    def sets(self, key: str, value: any) -> None:
        self.storage[key] = value
        self.save()

    def delete(self, key: str) -> None:
        del self.storage[key]
        self.save()

    def save(self) -> None:
        with open(self.file_dir, 'w+') as file:
            file.write(json.dumps(self.storage, indent=4))

    def get(self, key: str = None) -> dict | Any:
        if key:
            return self.storage[key]
        return self.storage


class JsonStorage:

    storage: dict[dict[OpenJson]] = dict()

    @classmethod
    def create(cls, folder_name: str, file_name: str) -> OpenJson:
        cls.storage[folder_name] = dict()
        cls.storage[folder_name][file_name] = OpenJson(folder_name, file_name)
        return cls.storage[folder_name][file_name]

    @classmethod
    def get(cls, folder_name: str = None, file_name: str = None) -> dict[dict[OpenJson]] | dict[OpenJson]:
        return_variable = cls.storage
        if folder_name:
            return_variable = cls.storage[folder_name]
        if file_name:
            return_variable = return_variable[file_name]
        return return_variable

    @classmethod
    def load_from_folder(cls, folder_name: str = None) -> dict[OpenJson]:
        cls.storage[folder_name]: dict[OpenJson] = dict()
        for json_file in os.listdir(f'json/{folder_name}'):
            file_name = json_file.split('.')[0]
            cls.storage[folder_name][file_name] = OpenJson(
                folder_name, file_name)
        return cls.storage[folder_name]
