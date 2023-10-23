from enums import TimeComplexity, SpaceComplexity
from AlgoRegistry import AlgoRegistry

class EnumError(Exception):
    pass

class AlgoNotFoundError(Exception):
    pass

class AlgoFactory:

    @staticmethod
    def get_Algorithm(time, space):
        if not isinstance(time,TimeComplexity):
            raise EnumError("Wrong Time Complexity provided")
        
        if not isinstance(space, SpaceComplexity):
            raise EnumError("Wrong Space Complexity provided")
        
        key = (time.value, space.value)

        registry = AlgoRegistry.get_instance()
        if registry.is_present(key):
            return registry.get_algorithms(key)
        else:
            raise AlgoNotFoundError('Could not find algorithm')



