from Shared import GameObject
from Shared import GameConstants


class Block(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game

        super().__init__(position, GameConstants.BLOCK_SIZE, sprite)


    def getGame(self):
        return self.__game
