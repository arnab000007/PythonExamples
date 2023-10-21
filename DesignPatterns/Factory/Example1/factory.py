
from UIFactory import UIFactoryFactory,SupportedPlatforms,UIFactory

class EnumError(Exception):
    pass


class Flutter:
    __supportedPlatforms = None

    def __init__(self, supportedPlatform):
        if not isinstance(supportedPlatform,SupportedPlatforms):
            raise EnumError("Wrong supportedPlatform type provided")
        
        self.__supportedPlatforms = supportedPlatform
    
    def setTheme(self):
        print('Setting theme')
    
    def setRefreshRate(self):
        print('Setting refresh rate')

    def createUIFactory(self) -> UIFactory:
        return UIFactoryFactory.getUIFactoryFromPlatform(self.__supportedPlatforms)
