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

            for block in game.getLevel().getBlocks():

                if person.intersects(block) == 0 and \
                        (person.getPosition()[0] >= 0 and person.getPosition()[0] < 700) \
                        and (person.getPosition()[1] >= 0 and person.getPosition()[1] < 600):
                    ##stop_position = person.getPosition()
                    ##print("intersect at" + str(stop_position))
                    ##break
                    person.move()
                else:
                    while person.intersects(block) or \
                            (person.getPosition()[0] < 0 or person.getPosition()[0] >= 800) or\
                            (person.getPosition()[1] < 0 or person.getPosition()[1] >= 600):
                        person.move()
                    break


            game.screen.blit(person.getSprite(), person.getPosition())

        for block in game.getLevel().getBlocks():
            game.screen.blit(block.getSprite(), block.getPosition())