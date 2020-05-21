from Shared import *
import pygame
import random


class Person(GameObject):
    def __init__(self, position, surface):

        self.__inMotion = 0
        self.__sdistance = GameConstants.SOCIAL_DISTANCE
        self.__speed = GameConstants.PERSON_SPEED
        self.dir_x, self.dir_y = 0, -1

        super().__init__(position, GameConstants.PERSON_SIZE, surface)


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
        pass

    def move(self, peopleGroup, blockGroup):

        self.rect = self.rect.move(self.__speed * self.dir_x, self.__speed * self.dir_y)

        if self.rect.top < self.getSize()[1]:
            self.rect = self.rect.move(self.__speed * 0, self.__speed * 1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.bottom > GameConstants.SCREEN_SIZE[1] - self.getSize()[1]:
            self.rect = self.rect.move(self.__speed * 0, self.__speed * -1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.left < self.getSize()[0]:
            self.rect = self.rect.move(self.__speed * 1, self.__speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.right > GameConstants.SCREEN_SIZE[0] - self.getSize()[0]:
            self.rect = self.rect.move(self.__speed * -1, self.__speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))

        if pygame.sprite.spritecollide(self, peopleGroup, False, None) \
                or pygame.sprite.spritecollide(self, blockGroup, False, None):
            self.rect = self.rect.move(self.__speed * -self.dir_x, self.__speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))