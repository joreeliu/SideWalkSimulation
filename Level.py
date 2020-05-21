import os
import fileinput
from Blocks import *
from Shared import *
import pygame


class Level:

    def __init__(self, game):
        self.__game = game
        self.__blocks = pygame.sprite.Group()
        self.__currentLevel = 0

    def getBlocks(self):
        return self.__blocks

    def loadNextLevel(self):
        pass

    def load(self, level):
        self.__currentLevel = level

        x, y = 0, 0

        for line in fileinput.input(os.path.join("Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBlock in line:
                if currentBlock == '1':
                    block = Block([x, y], load_image(GameConstants.SPRITE_BLOCK, GameConstants.BLOCK_SIZE), self)
                    self.__blocks.add(block)

                x += GameConstants.BLOCK_SIZE[0]

            x = 0
            y += GameConstants.BLOCK_SIZE[1]
