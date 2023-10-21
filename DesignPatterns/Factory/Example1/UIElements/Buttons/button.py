from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def getinfo(self) -> str:
        pass


class AndroidButton(Button):
    
    def getinfo(self) -> str:
        return 'This is Android button'
    

class IOSButton(Button):
    
    
    def getinfo(self) -> str:
        return 'This is IOS button'