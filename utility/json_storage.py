import json
import os

class OpenJson:

    def __init__(self, file_name:str) -> None:
        self.file_dir = f'json/{file_name}.json'

        with open(self.file_dir, 'r') as file:
            self.storage = dict()
            if os.path.getsize(self.file_dir) > 0:
                self.storage = json.loads(file.read())
    
    def sets(self, key:str, value:any) -> None:
        self.storage[key] = value
        self.save()
    
    def delete(self, key:str) -> None:
        del self.storage[key]
        self.save()
    
    def save(self) -> None:
        with open(self.file_dir, 'w+') as file:
            file.write(json.dumps(self.storage, indent=4))
    
    def get(self) -> dict:
        return self.storage

class JsonStorage:

    storage:dict[str, Test] = dict()

    @classmethod
    def create(cls, file_name:str) -> Test:
        test = Test(file_name)
        cls.storage[file_name] = test
        return test
    
    @classmethod
    def get(cls, file_name:str=None) -> Test | dict[Test]:
        return cls.storage[file_name] if file_name else cls.storage