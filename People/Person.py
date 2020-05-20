from Shared import *
import pygame
from Blocks import Block
import random

class Person(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = 0
        self.__sdistance = GameConstants.SOCIAL_DISTANCE

        super().__init__(position, GameConstants.PERSON_SIZE, sprite)
        self.setPosition([400, 250])


    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    def resetSpeed(self):
        self.setSpeed(3)

    def getSpeed(self):
        return self.__speed

    def isInMotion(self):
        return self.__inMotion

    def setMotion(self, isMoving):
        self.__inMotion = isMoving
        self.resetSpeed()

    def changeDirection(self, gameObject):
        pass

    def updatePosition(self):
        #self.setPosition(pygame.mouse.get_pos())
        pass

    def move(self):
        self.setSpeed(1)
        speed = self.getSpeed()
        current_pos = self.getPosition()
        direction = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
        self.setPosition([current_pos[0] + direction[0] * speed, current_pos[1] + direction[1]])

    def stop(self):
        self.setPosition([100, 100])
