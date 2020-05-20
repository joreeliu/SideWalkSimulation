

class GameObject:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def intersects(self, other):
        pass