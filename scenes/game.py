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
        print("drawing game scene")
        self.windowSurface.fill(WHITE)
        print(self.game_state.dealer_hand['cards'])
        print("initializing dealer hand")
        self.dealer_hand = Hand(cards=self.game_state.dealer_hand['cards'], x=100, y=100, windowSurface=self.windowSurface, basicFont=self.basicFont)
        print("initializing player hand")
        self.player_hand = Hand(cards=self.game_state.player_hand['cards'], x=100, y=300, windowSurface=self.windowSurface, basicFont=self.basicFont)
        [x.draw(self.windowSurface) for x in self.buttons]
        print("drawing dealer hand")
        self.dealer_hand.draw()
        print("drawing player hand")
        self.player_hand.draw()        

    def handle_events(self, event):
        pass

