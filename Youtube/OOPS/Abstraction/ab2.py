from abc import *

class Account(ABC):
    @abstractmethod
    def monety(self):
        pass
Account()


"""
If a class has an abc module 
and it extends with ABC class and it Have atleast one @abstract method
We are nit able to create a object
"""

"""
To resolve this
The child is resposible for all the object creation and execution
"""