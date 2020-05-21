import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, position, size, surface):
        super().__init__()
        self.__position = position
        self.__size = size
        self.__surface = surface
        self.rect = self.__surface.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1] + size[1]

    def get_rect(self):
        return self.rect

    def setPosition(self, position):
        self.__position = position
        self.rect.left = position[0]
        self.rect.top = position[1] + self.__size[1]

    def getPosition(self):
        return self.rect.left, self.rect.top - self.__size[1]

    def getSize(self):
        return self.__size

    def getSurface(self):
        return self.__surface