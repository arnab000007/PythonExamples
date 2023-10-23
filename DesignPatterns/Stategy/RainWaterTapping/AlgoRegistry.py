from multiprocessing import Lock
from function import RainWaterTappingInterface, RainWaterTappingAlgorithm1, RainWaterTappingAlgorithm2, RainWaterTappingAlgorithm3

class AlgoRegistry:

    #Class Variables
    __instance = None
    __lock: Lock = Lock()

    def __init__(self):
        '''Virtual Private constructor'''

        if AlgoRegistry.__instance != None:
            raise Exception('This is a Singleton class instance')
        else:
            self.__registry = {}
            self.__registeralgo()
            AlgoRegistry.__instance = self


    @staticmethod
    def get_instance():

        if AlgoRegistry.__instance == None:
            with AlgoRegistry.__lock:
                if AlgoRegistry.__instance == None:
                    AlgoRegistry()
        
        return AlgoRegistry.__instance
    
    def is_present(self, key) -> bool:
        return key in self.__registry
    
    
    def get_algorithms(self, key) -> RainWaterTappingInterface: 
        if key not in self.__registry:
            return None

        return self.__registry[key]

    def add_algorithms(self, key, obj: RainWaterTappingInterface) -> None:
        self.__registry[key] = obj


    def __registeralgo(self):
        self.__registry[('N2','1')] = RainWaterTappingAlgorithm1()
        self.__registry[('N','N')] = RainWaterTappingAlgorithm2()
        self.__registry[('N','1')] = RainWaterTappingAlgorithm3()