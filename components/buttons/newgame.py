# inherits from button and handles the click event
from components.buttons.button import Button
from config import *
import pygame

class NewGameButton(Button):
    def __init__(self, basicFont, game_state, callback):
        super().__init__(pygame.Rect(100, 100, 100, 50), "New Game", RED, WHITE, basicFont, callback)
        self.game_state = game_state    