import random
input_game=["Null","x","o","x","o","x","o","x","o","x"]

def board(input_game):
	print(input_game[7]+"|"+input_game[8]+"|"+input_game[9])
	print(input_game[4]+"|"+input_game[5]+"|"+input_game[6])
	print(input_game[1]+"|"+input_game[2]+"|"+input_game[3])

#board(input_game)

def Player_input():
	marker=""
	while marker != "x" and marker !="o":
		marker=input("player1: please chose your marker")
		if marker=="x":
			return ("x","o")
		else:
			return ("o","x")
#player_1,player_2=player_input()
#print(player_1+"is player 1 symbol")
#print(player_2+"is player 2 symbol")
def put_marker(input_game,marker,position):
	input_game[position]=marker

def win(input_game,marker):
	return ((input_game[1]==input_game[2]==input_game[3]==marker)or
	(input_game[4]==input_game[5]==input_game[6]==marker)or
	(input_game[7]==input_game[8]==input_game[9]==marker)or
	(input_game[7]==input_game[5]==input_game[3]==marker)or
	(input_game[1]==input_game[5]==input_game[9]==marker)or
	(input_game[1]==input_game[4]==input_game[7]==marker)or
	(input_game[2]==input_game[5]==input_game[8]==marker)or
	(input_game[3]==input_game[6]==input_game[9]==marker))

#print(win(input_game,'x'))
def chose_player():
	player=random.randint(1,2)
	if player==1:
		return 'player_1'
	else:
		return 'player_2'

def space(input_game,position):
	return input_game[position]== " "

def full_board_check(input_game):
	for i in range(1,10):
		if space(input_game,i):
			return False
	return True

def player_choice(input_game):
	position=0
	while position not in [1,2,3,4,5,6,7,8,9] or not space(input_game,position):
		position=int(input("Please Chose Your Position(1-9) On NumPad:"))
	return position

def play_agin():
	choice=input("would you like to play again[Y/N]:")
	return choice=="Y"
	
while True:
	the_board=[" "]*10
	player_1,player_2=Player_input()
	print(player_1,"is player_1  sign")
	print(player_2,"is Player_2 sign")
	
	turn=chose_player()
	print(turn+"will play first")
	
	play_game=input("Ready to play[Y/N]")
	if play_game=='Y':
		game_on=True
	else:
		game_on=False
	while game_on:
		if turn=='player_1':
			board(the_board)
			position=player_choice(the_board)
			put_marker(the_board,player_1,position)
			if win(the_board,player_1):
				board(the_board)
				print("Player 1 has won")
				game_on=False
			else:
				if full_board_check(the_board):
					board(the_board)
					print("game Draw")
					game_on=False
				else:
					turn="player_2"
		else:
			board(the_board)
			position=player_choice(the_board)
			put_marker(the_board,player_2,position)
			if win(the_board,player_2):
				board(the_board)
				print("Player 2 has won")
				game_on=False
			else:
				if full_board_check(the_board):
					board(the_board)
					print("game Draw")
					game_on=False
				else:
					turn="player_1"
			
	if not play_agin():
		break
	
	