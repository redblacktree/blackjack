from components.card import Card
from config import *

class Hand():
    def __init__(self, cards, x, y, windowSurface, basicFont):
        #    def __init__(self, card, x, y, windowSurface, basicFont):
        print("initializing hand")
        self.cards = [Card(card, x + CARD_OFFSET, y, windowSurface, basicFont) for (i, card) in enumerate(cards)]
        print(self.cards)
        self.x = x
        self.y = y
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        print("drawing hand")
        self.draw()

    def draw(self):
        for card in self.cards:
            card.draw()
            