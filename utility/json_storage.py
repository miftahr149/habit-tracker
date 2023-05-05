import json
import os


class OpenJson:

    def __init__(self, file_name: str) -> None:
        self.file_dir = f'json/{file_name}.json'

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

    def get(self) -> dict:
        return self.storage


class JsonStorage:

    storage: dict[dict[OpenJson]] = dict()

    @classmethod
    def create(cls, file_name: str, folder: str = 'default') -> OpenJson:
        cls.storage[type_storage][file_name] = OpenJson(file_name)
        return cls.storage[type_storage][file_name]

    @classmethod
    def get(cls, file_name: str = None, folder: str = 'default') -> OpenJson | dict[OpenJson]:
        return cls.storage[type_storage][file_name] if file_name else cls.storage

    @classmethod
    def load_from_folder(cls, folder: str = None) -> dict[OpenJson]:
        json_dict: dict[OpenJson] = dict()
        for json_file in os.listdir(folder):
            file_name = json_file.split('.')[0]
            json_dict[file_name] = OpenJson(file_name)
        return json_dict
