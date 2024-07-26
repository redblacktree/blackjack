# game scene with player and dealer hands, hit, stand, and double down buttons
from config import *
from components.hand import Hand

class GameScene():
    def __init__(self, windowSurface, basicFont, game_state):
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        self.game_state = game_state
        self.buttons = []
        windowSurface.fill(WHITE)
        for button in self.buttons:
            button.draw(self.windowSurface)

    def draw(self):
        self.windowSurface.fill(WHITE)
        self.dealer_hand = Hand(cards=self.game_state.dealer_hand['cards'], x=DEALER_CARDS_X, y=DEALER_CARDS_Y, windowSurface=self.windowSurface, basicFont=self.basicFont, hide_first_card=True)
        self.player_hand = Hand(cards=self.game_state.player_hand['cards'], x=PLAYER_CARDS_X, y=PLAYER_CARDS_Y, windowSurface=self.windowSurface, basicFont=self.basicFont)
        [x.draw(self.windowSurface) for x in self.buttons]
        self.dealer_hand.draw()
        self.player_hand.draw()        

    def handle_events(self, event):
        pass
