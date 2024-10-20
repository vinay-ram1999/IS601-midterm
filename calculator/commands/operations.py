from abc import ABC, abstractmethod

class Operation(ABC):
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for arg in kwargs.keys():
                setattr(self, arg, kwargs[arg])

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class BuiltInOperation(ABC):
    opr_handler = None

    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for arg in kwargs.keys():
                setattr(self, arg, kwargs[arg])

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass