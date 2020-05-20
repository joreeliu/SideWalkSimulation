from Shared import *
import pygame

from Shared import *
from People import *
from Scenes import *
from Level import Level


class Breakout:
    def __init__(self):
        self.__level = Level(self)
        self.__level.load(0)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Urban Simulation")

        self.__clock = pygame.time.Clock()
        self.__clock.tick(40)

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF, 32)

        self.__People = [Person((0, 0), load_image(GameConstants.SPRITE_PERSON, GameConstants.PERSON_SIZE), self)]

        pygame.mouse.set_visible(0)

        self.__scenes = (
            UrbanScene(self),
        )

        self.__currentScene = 0

        self.__sounds = ()


    def start(self):
        while 1:
            self.__clock.tick(100)

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


Breakout().start()