from abc import *
class Bank(ABC):

    @abstractmethod
    def bal(self):
        print("Bank Level Balance")

# Not bale to create obj 
# Child class is responsible