from components.card import Card, CARD_SIZE
from config import *

class Hand():
    def __init__(self, cards, x, y, windowSurface, basicFont, hide_first_card=False):
        self.cards = [Card(card, x + i * CARD_OFFSET, y, windowSurface, basicFont, hidden=(hide_first_card and i == 0)) for (i, card) in enumerate(cards)]
        self.x = x
        self.y = y
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        self.draw()

    def draw(self):
        for card in self.cards:
            card.draw()
