import os


class GameConstants:
    SCREEN_SIZE = [1000, 800]
    PERSON_SIZE = [50, 50]
    BLOCK_SIZE = [50, 50]

    SPRITE_PERSON = os.path.join("Assets", "Person.png")
    SPRITE_BLOCK = os.path.join("Assets", "iron.png")

    SOCIAL_DISTANCE = 2
    PERSON_SPEED = 50
    TICK = 5000