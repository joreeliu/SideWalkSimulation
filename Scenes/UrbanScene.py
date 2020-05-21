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
        people = game.getPeople()

        for person in game.getPeople():
            people.remove(person)
            person.move(people, game.getLevel().getBlocks())
            people.add(person)

        for person in people:

            game.screen.blit(person.getSurface(), person.getPosition())

        for block in game.getLevel().getBlocks():
            game.screen.blit(block.getSurface(), block.getPosition())