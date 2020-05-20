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

    def render(self):
        super().render()

        game = self.getGame()

        for person in game.getPeople():
            person.updatePosition()

            game.screen.blit(person.getSprite(), person.getPosition())

        for block in game.getLevel().getBlocks():
            game.screen.blit(block.getSprite(), block.getPosition())