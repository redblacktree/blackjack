# class to maintain the game state
# states are: menu, new_game, player_turn, dealer_turn, game_over
import pygame
import requests
from scenes.menu import MenuScene
from scenes.game import GameScene

class GameState():
    def __init__(self, scenes):
        self.scenes = scenes
        self.scene = "menu"
        self.event_handlers = []
        self.deck = None
        self.dealer_hand = None
        self.player_hand = None
        
    def new_game(self):        
        # deal deck of cards
        self.deck = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        # deal dealer hand
        self.dealer_hand = requests.get('https://deckofcardsapi.com/api/deck/' + self.deck.json()['deck_id'] + '/draw/?count=2').json()
        # deal player hand
        self.player_hand = requests.get('https://deckofcardsapi.com/api/deck/' + self.deck.json()['deck_id'] + '/draw/?count=2').json()
        self.set_scene("game")

    def get_scene(self):
        return self.scene
    
    def set_scene(self, scene_name):
        self.scene = self.scenes[scene_name]
        self.scene.draw()
        self.event_handlers = [self.scene.handle_events]

    def handle_events(self, event):        
        for event_handler in self.event_handlers:
            event_handler(event)

scenes = {}
game_state = GameState(scenes=scenes)
