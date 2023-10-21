from abc import ABC, abstractmethod
from enum import Enum
from UIElements.Buttons.button import Button, AndroidButton,IOSButton

class SupportedPlatforms(Enum):
    ANDROID = 1
    IOS = 2

class UIFactory(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createMenu(self):
        pass
    
    @abstractmethod
    def createDropdown(self):
        pass



class AndroidUIFactory(UIFactory):

    def createButton(self) -> AndroidButton:
        print('Creating Android Button')
        return AndroidButton()

    def createMenu(self):
        print('Creating Android Menu')
    
    def createDropdown(self):
        print('Creating Android Dropdown')


class IOSUIFactory(UIFactory):
    def createButton(self) -> IOSButton:
        print('Creating IOS Button')
        return IOSButton()

    def createMenu(self):
        print('Creating IOS Menu')
    
    def createDropdown(self):
        print('Creating IOS Dropdown')
    

class UIFactoryFactory:

    @staticmethod
    def getUIFactoryFromPlatform(supportedPlatforms):
        if supportedPlatforms == SupportedPlatforms.ANDROID:
            return AndroidUIFactory()
        
        if supportedPlatforms == SupportedPlatforms.IOS:
            return IOSUIFactory()
        
        return None