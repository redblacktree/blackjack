import os
import pygame
import requests
from config import *

class Card():
    def __init__(self, card, x, y, windowSurface, basicFont, hidden=False):
        self.card = card
        self.x = x
        self.y = y        
        namehint = self.card['image'].split('/')[-1]
        self.card_image = pygame.image.load(self.get_image_from_url(self.card['image']), namehint)
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        self.hidden = hidden

    def get_image_from_url(self, url):
        with (open(os.path.join(os.path.dirname(__file__), 'temp.png'), 'wb')) as f:
            f.write(requests.get(url).content)
        return os.path.join(os.path.dirname(__file__), 'temp.png')

    def draw(self):
        if self.hidden:
            card_back_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'card_back.png'))
            cardRect = card_back_image.get_rect()
        else:
            cardRect = self.card_image.get_rect()
        cardRect.centerx = self.x
        cardRect.centery = self.y
        self.windowSurface.blit(self.card_image if not self.hidden else card_back_image, cardRect)
