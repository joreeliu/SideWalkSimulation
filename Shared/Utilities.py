import pygame


def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)