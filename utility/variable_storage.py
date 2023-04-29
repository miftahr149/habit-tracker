class VariableStorage:

    __storage:dict[str, any] = dict()

    @classmethod
    def add(cls, key: str, item: any) -> None:
        cls.__storage[key] = item
    
    @classmethod
    def get(cls, key: str) -> any:
        try:
            return cls.__storage[key]
        except KeyError:
            print(f"there is no key '{key}'")