from typing import Callable


class Stack:
    
    def __init__(self, func_list: list[Callable]) -> None:
        self.func_list = func_list

    def __call__(self) -> None:
        for func in self.func_list:
            func()


class FunctionStorage:

    __storage = dict()

    def __init__(self, func_list: list[Callable], name: str) -> None:
        self.__storage[name] = Stack(func_list)

    @classmethod
    def get(cls, name: str = None) -> Stack:
        if name == None:
            return cls.__storage
        
        try:
            return cls.__storage[name]
        except KeyError:
            print(f'There is no function {name}')