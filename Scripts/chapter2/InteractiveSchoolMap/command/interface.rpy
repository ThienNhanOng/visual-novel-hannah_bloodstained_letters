init -100 python:
    #abc = abstract base class
    #importing abstract base class module
    from abc import ABC, abstractmethod

    #so commands must implement execute
    class CommandInterface(ABC):
        @abstractmethod
        def execute(self):
            pass