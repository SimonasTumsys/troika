import os, sys
import pygame
import random
from pygame import *


class Card(object):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.get_path()
        self.img = self.load_img()
        self.rect = self.img.get_rect()
        self.name = self.get_name()
        self.playable = True
    
    def get_name(self):
        if self.rank <= 10:
            name = str("{}_of_{}".format(self.rank, self.suit))
        elif self.rank == 11:
            name = str("{}_of_{}".format('jack', self.suit))
        elif self.rank == 12:
            name = str("{}_of_{}".format('queen', self.suit))
        elif self.rank == 13:
            name = str("{}_of_{}".format('king', self.suit))
        elif self.rank == 14:
            name = str("{}_of_{}".format('ace', self.suit))
        return name
    
        
    def get_path(self):
        name = self.get_name()
        path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/cards/', name + '.png')
        return path
    
    def setPlayable(state):
        self.playable = state

    def load_img(self, colorkey=None):
        path = self.get_path()
        try:
            image = pygame.image.load(path)
        except pygame.error:
            print('Cannot load image:', path)
            raise SystemExit
        image = pygame.transform.scale(image, (100, 150))
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
        


class Deck(object):
    def __init__(self):
        self.cards_in_deck = []
        self.build()
        
    def build(self):
        for s in ['diamonds', 'hearts', 'spades', 'clubs']:
            for r in range(2, 15):
                card = Card(r, s)
                self.cards_in_deck.append(card)
                

    
    def draw(self):
        drawn_card = random.choice(self.cards_in_deck)
        self.cards_in_deck.remove(drawn_card)
        return drawn_card
        



class Player(object):
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.score = 0
        self.hand = []
        
    def update_score(self):
        self.score += 1
        
    def disconnect(self):
        pass
        
    def get_score(self):
        return self.score
        
    def get_name(self):
        return self.name
    
    def get_ip(self):
        return self.ip




class Board(object):

    def __init__(self):
        self.cards_played = []
        self.center_coord()
        self.deck_container_coord()
        
    def get_path(self):
        name = 'board'
        path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/board/', name + '.png')
        return path
    
    def get_bottom_half_path(self):
        name = 'board_bottom_half'
        b_path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/board/', name + '.png')
        return b_path
    
    def get_top_half_path(self):
        name = 'board_top_half'
        t_path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/board/', name + '.png')
        return t_path    
        
    def load_img(self, colorkey=None):
        path = self.get_path()
        try:
            image = pygame.image.load(path)
        except pygame.error:
            print('Cannot load image:', path)
            raise SystemExit
        image = image.convert_alpha()
        
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
        
    def load_bottom_img(self, colorkey=None):
        b_path = self.get_bottom_half_path()
        try:
            image = pygame.image.load(b_path)
        except pygame.error:
            print('Cannot load image:', b_path)
            raise SystemExit
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
        
    def load_top_img(self, colorkey=None):
        t_path = self.get_top_half_path()
        try:
            image = pygame.image.load(t_path)
        except pygame.error:
            print('Cannot load image:', t_path)
            raise SystemExit
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
            
    def center_coord(self):
        width = 60
        height = 50
        left = 510
        top = 275
        center_coord = pygame.Rect((left, top), (width, height))
        return center_coord
        
    def deck_container_coord(self):
        width = 50
        height = 100
        left = 350
        top = 200
        deck_container_coord = pygame.Rect((left, top), (width, height))
        return deck_container_coord

    
    

class Button(object):
    def __init__(self):
        pass

    def get_ta_path(self):
        name = 'take_all'
        ta_path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/', name + '.png')
        return ta_path
   
    def get_et_path(self):
        name = 'end_turn'
        et_path = os.path.join('/home/simas/Documents/Python/cardgames/troika/img/', name + '.png')
        return et_path 
    
    def load_ta_img(self, colorkey=None):
        ta_path = self.get_ta_path()
        try:
            image = pygame.image.load(ta_path)
        except pygame.error:
            print('Cannot load image:', ta_path)
            raise SystemExit
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
        
    def load_et_img(self, colorkey=None):
        et_path = self.get_et_path()
        try:
            image = pygame.image.load(et_path)
        except pygame.error:
            print('Cannot load image:', et_path)
            raise SystemExit
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image





































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

