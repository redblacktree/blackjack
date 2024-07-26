import os
import pygame
import requests
from config import *
import pygame.transform

CARD_SIZE = (50, 75)

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

    def get_card_back_image(self):
        url = 'https://deckofcardsapi.com/static/img/back.png'
        with (open(os.path.join(os.path.dirname(__file__), 'temp_back.png'), 'wb')) as f:
            f.write(requests.get(url).content)
        return os.path.join(os.path.dirname(__file__), 'temp_back.png')

    def draw(self):
        if self.hidden:
            card_back_image = pygame.image.load(self.get_card_back_image())
            card_back_image = pygame.transform.scale(card_back_image, CARD_SIZE)
            cardRect = card_back_image.get_rect()
        else:
            card_image = pygame.transform.scale(self.card_image, CARD_SIZE)
            cardRect = card_image.get_rect()
        cardRect.centerx = self.x
        cardRect.centery = self.y
        self.windowSurface.blit(card_image if not self.hidden else card_back_image, cardRect)
