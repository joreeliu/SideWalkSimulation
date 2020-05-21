from Shared import *
import pygame

from Shared import *
from People import *
from Scenes import *
from Level import Level
import random


class Breakout:
    def __init__(self):
        self.__level = Level(self)
        self.__level.load(0)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Urban Simulation")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF, 32)

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)

        self.__People = pygame.sprite.Group()

        for i in range(10):
            self.__People.add(
                Person((random.randint(1, GameConstants.SCREEN_SIZE[0]), random.randint(1, GameConstants.SCREEN_SIZE[0])), load_image(GameConstants.SPRITE_PERSON, GameConstants.PERSON_SIZE), self))

        self.__scenes = (
            UrbanScene(self),
        )

        self.__currentScene = 0

        self.__sounds = ()


    def start(self):

        while 1:

            self.__clock.tick(GameConstants.TICK)
            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()


    def changeScene(self, scene):
        self.__currentScene = scene

    def getPeople(self):
        return self.__People

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]
        sound.stop()
        sound.play()

    def getLevel(self):
        return self.__level

    def reset(self):
        pass

if __name__ == '__main__':
    Breakout().start()