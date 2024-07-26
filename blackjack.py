# a blackjack game written in pygame that uses a card api to get images of cards
import pygame
import sys
import requests
from pygame.locals import *
from config import *
from gamestate import game_state
from scenes.menu import MenuScene
from scenes.game import GameScene

# set up pygame
pygame.init()

# set up the fonts 
basicFont = pygame.font.SysFont(None, 48)

# set up the window
windowSurface = pygame.display.set_mode((1440, 1080), 0, 32)

game_state.scenes["menu"] = MenuScene(windowSurface, basicFont, game_state)
game_state.scenes["game"] = GameScene(windowSurface, basicFont, game_state)
game_state.set_scene("menu")

# black jack game
def blackjack():
    # set up game loop
    while True:
        # draw the window onto the screen
        pygame.display.update()
       
        # check for the QUIT event
        for event in pygame.event.get():
            game_state.handle_events(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            
        
blackjack()