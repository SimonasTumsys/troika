def rules():
    turn = 1
    r_g_z_x = random.choice(g_z_x)
    r_g_z_y = random.choice(g_z_y)
    while turn == 1:
        if card.rect.collidepoint(pos):
	        if len(board.cards_played) == 0:
	            play_card()
	            if card.rank == 10:
                    board.cards_played.clear()
                    gameDisplay.blit(board_top_half, (0,25))
                    turn = 1
                        
                elif card.rank == 3:
                    board.cards_played.clear()
                    gameDisplay.blit(board_top_half, (0,25))
                    turn = 1
	            
	        elif len(board.cards_played) > 0:
	            if card.rank == 10:
	                board.cards_played.clear()
	                gameDisplay.blit(board_top_half, (0,25))
	                turn = 1
	                
	            elif card.rank == 2:
	                play_card()
	                turn = 2	        
	                
	            elif card.rank == 3:
	                play_card()
	                turn = 2
	            
	            elif card.rank == 6:
	                if board.cards_played[-1].rank < 6:
	                    play_card()
	                    turn = 2
	                    
	                
	            elif board.cards_played[-1].rank < card.rank:
	                play_card()
	                turn = 2
	            
	            elif board.cards_played[-1].rank == card.rank:
	                if len(board.cards_played) >= 3:
	                    if board.cards_played[-3].rank == board.cards_played[-2].rank and board.cards_played[-2].rank == board.cards_played[-1].rank and board.cards_played[-1].rank == card.rank:
                            play_card()
                            board.cards_played.clear()
                            gameDisplay.blit(board_top_half, (0,25))
                            turn = 1
                    else:
                        play_card()
                        turn = 2
                else:
                    turn = 1        
                

    while turn == 2:
        if card.rect.collidepoint(pos):
            turn = 2
            if card.rank == board.cards_played[-1].rank:
                if len(board.cards_played) >= 3:
	                if board.cards_played[-3].rank == board.cards_played[-2].rank and board.cards_played[-2].rank == board.cards_played[-1].rank and board.cards_played[-1].rank == card.rank:
                        play_card()
                        board.cards_played.clear()
                        gameDisplay.blit(board_top_half, (0,25))
                        turn = 1
                else:
                    play_card()
                    turn = 2
            else:
                turn = 2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
