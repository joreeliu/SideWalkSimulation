
class Level:

    def __init__(self, game):
        self.__game = game
        self.__blocks = []
        self.__currentLevel = 0

    def getBlocks(self):
        return self.__blocks

    def loadNextLevel(self):
        pass

    def load(self, level):
        pass