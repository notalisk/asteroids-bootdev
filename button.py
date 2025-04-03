import pygame
from constants import *

class Button():
    def __init__(self, text, x, y, width, height):
        self.color = BUTTON_COLOR
        self.hover_color = BUTTON_HOVER_COLOR
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 36).render(text, True, self.color)
        self.hover_font = pygame.font.Font(None, 36).render(text, True, self.hover_color)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect, 2)
            screen.blit(self.hover_font, (self.rect.x + 10, self.rect.y + 10))
        else:
            pygame.draw.rect(screen, self.color, self.rect, 2)
            screen.blit(self.font, (self.rect.x + 10, self.rect.y + 10))
    
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            return True
        return False

