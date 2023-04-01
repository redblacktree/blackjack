# a blackjack game written in pygame that uses a card api to get images of cards
import pygame
import sys
import requests
from pygame.locals import *
from config import *
from gamestate import game_state
from scenes.menu import MenuScene
from scenes.game import GameScene


# def get_filelike_from_url(url):
#     return requests.get(url, stream=True).raw

# def draw_card(card, x, y):
#     card_url = get_filelike_from_url(card.json()['cards'][0]['image'])
#     card = pygame.image.load(card_url)
#     cardRect = card.get_rect()
#     cardRect.centerx = x
#     cardRect.centery = y
#     windowSurface.blit(card, cardRect)

# def draw_dealer_card(card, card_index):
#     draw_card(card, DEALER_CARDS_X + (card_index * CARD_OFFSET), DEALER_CARDS_Y)
    
# def draw_player_card(card, card_index):
#     draw_card(card, PLAYER_CARDS_X + (card_index * CARD_OFFSET), PLAYER_CARDS_Y)

# set up pygame
pygame.init()

# set up the fonts 
basicFont = pygame.font.SysFont(None, 48)

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)

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