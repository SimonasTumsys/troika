import pygame
import os
import sys
import random
from my_classes import Card, Deck, Board, Player, Button


# defining main instances
pygame.init()


deck = Deck()
board = Board()
player = Player('harry', 888) # OLD
players = {
    harry: Player('kusys', 888),
    harry: Player('bybis', 887),
    harry: Player('kiausai', 886),
    harry: Player('shliundra', 885)        
}

hand = player.hand # OLD

angles = [0, 5, 10, 15, 20, 25, 30, 35, 45,
          330, 335, 340, 345, 350, 355, 360]


# action functions
def draw_card():
    drawn_card = deck.draw()
    hand.append(drawn_card)
    return drawn_card


# display
display_width = 1280
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('troika')

crashed = False

# BOARD
board_img = board.load_img()
board_bottom_half = board.load_bottom_img()
board_top_half = board.load_top_img()
gameDisplay.blit(board_img, (0, 25))


game_zone = board.center_coord()

# board center coordinates
g_z_x = range(580, 640, 10)
g_z_y = range(250, 300, 5)


draw_card()
draw_card()
draw_card()
draw_card()

# buttons
take_all = Button()
ta_img = take_all.load_ta_img()
ta_rect = ta_img.get_rect()
ta_rect.center = (900, 250)
gameDisplay.blit(ta_img, ta_rect)


end_turn = Button()
et_img = end_turn.load_et_img()
et_rect = et_img.get_rect()
et_rect.center = (900, 180)
gameDisplay.blit(et_img, et_rect)


# HAND

def get_hand_card_pos():
    if len(hand) == 0:
        gameDisplay.blit(board_bottom_half, (0, 25))

    elif len(hand) == 2:
        x = 580
        y = 500
        for card in hand:
            card.img = card.load_img()
            card.rect = card.img.get_rect()
            card.rect.center = (x, y)
            display = gameDisplay.blit(card.img, card.rect)
            x += 100
    elif len(hand) == 4:
        x = 490
        y = 500
        for card in hand:
            card.img = card.load_img()
            card.rect = card.img.get_rect()
            card.rect.center = (x, y)
            display = gameDisplay.blit(card.img, card.rect)
            x += 101
    elif len(hand) == 1:
        x = 630
        y = 500
        for card in hand:
            card.img = card.load_img()
            card.rect = card.img.get_rect()
            card.rect.center = (x, y)
            display = gameDisplay.blit(card.img, card.rect)
    elif len(hand) == 3:
        x = 540
        y = 500
        for card in hand:
            card.img = card.load_img()
            card.rect = card.img.get_rect()
            card.rect.center = (x, y)
            display = gameDisplay.blit(card.img, card.rect)
            x += 100

    return


get_hand_card_pos()



def play_card(card, hand):
    board.cards_played.append(card)
    hand.remove(card)

    angle = random.choice(angles)
    gameDisplay.blit(pygame.transform.rotozoom(
        card.img, angle, 0.55), (r_g_z_x, r_g_z_y))
    gameDisplay.blit(board_bottom_half, (0, 25))
    get_hand_card_pos()

    
    # Check if another same rank card is in hand

    # Option to play another card

    # If card in hand - drop card, allow to play another card.
    
    return


def turn(player):
    for card in hand:
        if card.rect.collidepoint(pos) and card.playable == True:
            if len(board.cards_played) == 0:
                if card.rank == 10:
                    play_card(card)
                    board.cards_played.clear()
                    gameDisplay.blit(board_top_half, (0, 25))
                    

                elif card.rank == 3:
                    play_card(card)
                    board.cards_played.clear()
                    gameDisplay.blit(board_top_half, (0, 25))
                    
                else:
                    play_card(card)
                    

            elif len(board.cards_played) > 0:
                if card.rank == 10:
                    play_card(card)
                    board.cards_played.clear()
                    gameDisplay.blit(board_top_half, (0, 25))
                    

                elif card.rank == 2 or card.rank == 3:
                    play_card(card)
                    

                elif card.rank == 6:
                    if board.cards_played[-1].rank < 6:
                        play_card(card)
                            

                elif board.cards_played[-1].rank < card.rank:
                    if not board.cards_played[-1].rank == 6:
                        play_card(card)
                        
                elif board.cards_played[-1].rank == 6:
                    if card.rank < 6:
                        play_card(card)


                elif board.cards_played[-1].rank == card.rank:
                    if len(board.cards_played) >= 3:
                        if board.cards_played[-3].rank == board.cards_played[-2].rank and board.cards_played[-2].rank == board.cards_played[-1].rank and board.cards_played[-1].rank == card.rank:
                            play_card(card)
                            board.cards_played.clear()
                            gameDisplay.blit(board_top_half, (0, 25))
                            
                            
                    else:
                        play_card(card)
                
    if et_rect.collidepoint(pos):
        print('End turn')


# def set_playable():
#     test_hand = []
#         for card in hand:
#             test_hand.append(card.rank)
#             if len(board.cards_played) == 0:
#                 card.playable = True
#             elif len(board.cards_played) > 0:
#                 if card.rank == 10:
#                     card.playable = True
#                 elif card.rank == 2:
#                     card.playable = True
#                 elif card.rank == 3:
#                     card.playable = True
#                 elif card.rank == 6:
#                     if board.cards_played[-1].rank < 6: 

#                 elif board.cards_played[-1].rank < card.rank:
#                     if not board.cards_played[-1].rank == 6:
                        
#                 elif board.cards_played[-1].rank == 6:
#                     if card.rank < 6:

#                 elif board.cards_played[-1].rank == card.rank:
#                     if len(board.cards_played) >= 3:
#                         if board.cards_played[-3].rank == board.cards_played[-2].rank and board.cards_played[-2].rank == board.cards_played[-1].rank and board.cards_played[-1].rank == card.rank:
                            
#                     else:
                



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


            r_g_z_x = random.choice(g_z_x)
            r_g_z_y = random.choice(g_z_y)
            turn()
            


    pygame.display.update()
