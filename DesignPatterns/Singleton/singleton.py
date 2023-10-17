class Singleton:

    #Class Variables
    __instance = None

    @staticmethod
    def get_instance():

        if Singleton.__instance == None:
            Singleton()
        
        return Singleton.__instance
    

    def __init__(self):
        '''Virtual Private constructor'''

        if Singleton.__instance != None:
            raise Exception('This is a Singleton class instance')
        else:
            Singleton.__instance = self


s1 = Singleton.get_instance()
print(s1)

s2 = Singleton.get_instance()
print(s2)








            