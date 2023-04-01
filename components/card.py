import os
import pygame
import requests
from config import *

class Card():
    def __init__(self, card, x, y, windowSurface, basicFont):
        print("initializing card")
        self.card = card
        self.x = x
        self.y = y        
        print("desperately trying to load card image")
        print(pygame.image.get_extended())
        namehint = self.card['image'].split('/')[-1]
        print(namehint)
        print(self.card)
        self.card_image = pygame.image.load(self.get_image_from_url(self.card['image']), namehint)
        self.windowSurface = windowSurface
        self.basicFont = basicFont

    def get_image_from_url(self, url):
        with (open(os.path.join(os.path.dirname(__file__), 'temp.png'), 'wb')) as f:
            f.write(requests.get(url).content)
        return os.path.join(os.path.dirname(__file__), 'temp.png')

    def draw(self):
        cardRect = self.card_image.get_rect()
        cardRect.centerx = self.x
        cardRect.centery = self.y
        self.windowSurface.blit(self.card_image, cardRect)