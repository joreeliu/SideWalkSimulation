from Scenes.Scene import Scene
import pygame


class UrbanScene(Scene):

    def __init__(self, game):
        super().__init__(game)

    def handleEvents(self, events):
        super().handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

