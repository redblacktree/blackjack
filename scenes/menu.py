# Menu scene for the game
from components.buttons.newgame import NewGameButton
from pygame.locals import *
from config import *

class MenuScene():
    def __init__(self, windowSurface, basicFont, game_state):
        self.windowSurface = windowSurface
        self.basicFont = basicFont
        self.game_state = game_state
        self.buttons = []
        self.buttons.append(NewGameButton(basicFont=self.basicFont, game_state=game_state, callback=self.new_game))
        for button in self.buttons:
            button.draw(self.windowSurface)

    def draw(self):
        self.windowSurface.fill(WHITE)
        [x.draw(self.windowSurface) for x in self.buttons]

    def handle_events(self, event):            
        if event.type == MOUSEBUTTONUP:
            for button in self.buttons:
                if button.is_clicked(event):
                    return button.clicked(event)
                
    def new_game(self, event):
        self.game_state.new_game()
