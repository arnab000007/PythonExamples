from abc import ABC, abstractmethod

# Abstract facory interface
class GameFactory(ABC):
    @abstractmethod
    def create_character(self,):
        pass
    
    @abstractmethod
    def create_weapon(self,):
        pass

# Create character for Fantasy player
class FantasyGameFactory(GameFactory):
    def create_character(self):
        return ElfCharacter()
    
    def create_weapon(self):
        return Sword()

# Create character for Scify player

class ScifyGameFactory(GameFactory):
    def create_character(self):
        return RobotCharacter()
    
    def create_weapon(self):
        return Laser()


# Create character interface

class Character(ABC):

    @abstractmethod
    def info(self):
        pass

# Create Weapon interface

class Weapon(ABC):
    @abstractmethod
    def info(self):
        pass


# Create ElfCharacter
class ElfCharacter(Character):
    def info(self):
        return "Elf Character"

#Create Robot Character 
class RobotCharacter(Character):
    def info(self):
        return "Robot Character"


# Create Sword Weapon
class Sword(Weapon):
    def info(self):
        return "Sword Weapon"

# Create Laser Weapon
class Laser(Weapon):
    def info(self):
        return "Laser Weapon"

def create_factory(factory):
    character = factory.create_character()
    weapon = factory.create_weapon()
    # print(f"Created {character.info()} with {weapon.info()}")
    return character, weapon

fantasy_factory = FantasyGameFactory()
fan_character, fan_weapon = create_factory(fantasy_factory)
print(f"Created {fan_character.info()} with {fan_weapon.info()}")

sci_factory = ScifyGameFactory()
sci_character, sci_weapon = create_factory(sci_factory)
print(f"Created {sci_character.info()} with {sci_weapon.info()}")



