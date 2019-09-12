# Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

print ('Welcome to Heads or Tails')

import random

def choose_first ():
	if random.randint (0,1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

choose_first ()

myList = ["heads", "tails"]

start_game = input ('Are you ready to play? Enter Yes or No')

def play_again ():
	return input ('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

if start_game.lower()[0] == 'y':
	begin_game = True
else:
	begin_game = False

# Player 1's turn.
while begin_game:
	turn = choose_first()
	if turn == 'Player 1':
		random.choice(myList)

		if (myList) == "heads":
			print ('Heads')
		else:
			print ('Tails')

	else: # Player 2's Turn 
		if (myList) == "heads":
			print ('Heads')
		else:
			print ('Tails')
			if "heads" or "tails" >= 10:
				break 



