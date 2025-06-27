
from abc import ABC, abstractmethod

class Speed(ABC):
    @abstractmethod
    def delay(self) -> int: ...
    @abstractmethod
    def increment(self) -> int: ...

class Off(Speed):
    def delay(self):     
        return 200
    def increment(self): 
        return   0

class Low(Speed):
    def delay(self):     
        return 150
    def increment(self): 
        return   8

class Med(Speed):
    def delay(self):     
        return  90
    def increment(self): 
        return  16

class High(Speed):
    def delay(self):     
        return  40
    def increment(self): 
        return  24

# map 0..3 → strategy
SPEED = {0: Off(), 1: Low(), 2: Med(), 3: High()}
