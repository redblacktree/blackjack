# button class and button event handling
import pygame
from pygame.locals import *

class Button(object):
    def __init__(self, rect, text, color, text_color, font, callback):
        self.rect = rect
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = font
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.centerx = self.rect.centerx
        text_rect.centery = self.rect.centery
        surface.blit(text, text_rect)

    def is_clicked(self, event):
        if event.type == MOUSEBUTTONUP:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

    def is_mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
    
    def clicked(self, event):
        self.callback(event)