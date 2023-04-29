from typing import Callable


class Stack:
    
    def __init__(self, func_list: list[Callable]) -> None:
        self.func_list = func_list

    def __call__(self) -> None:
        for func in self.func_list:
            func()


class FunctionStorage:

    __storage:dict[str, Stack] = dict()
    
    @classmethod
    def add(self, func_list: list[Callable], key: str) -> None:
        self.__storage[key] = Stack(func_list)

    @classmethod
    def get(cls, key: str = None) -> Stack:
        if key == None:
            return cls.__storage
        
        try:
            return cls.__storage[key]
        except KeyError:
            print(f'There is no function {key}')
    
    @classmethod
    def execute(cls, key: str) -> None:
        try:
            cls.__storage[key]()
        except KeyError():
            print(f'There is no function {key}')