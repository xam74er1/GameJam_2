import pygame


class Walls:
    def __init__(self, pos, size, color=(0, 0, 0), alpha=128):
        self.surface = pygame.Surface((size[0], size[1]))
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.size = size
        self.pos = pos
        self.color = color
        self.surface.fill(color)
        self.surface.set_alpha(alpha)
        self.alpha = alpha