import os


class GameConstants:
    SCREEN_SIZE = [800, 800]
    PERSON_SIZE = [5, 5]
    BLOCK_SIZE = [50, 50]

    SPRITE_PERSON = os.path.join("Assets", "Person.png")
    SPRITE_BLOCK = os.path.join("Assets", "iron.png")

    SOCIAL_DISTANCE = 2
    PERSON_SPEED = 2
    TICK = 5000