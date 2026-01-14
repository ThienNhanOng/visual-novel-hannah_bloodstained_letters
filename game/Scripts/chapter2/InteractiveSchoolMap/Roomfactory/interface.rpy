#interface to enter rooms
init -100 python:
    from abc import ABC, abstractmethod

    class Enterable(ABC):
        @abstractmethod
        def enter(self):
            """All rooms must know how to be 'entered' from the map."""
            pass