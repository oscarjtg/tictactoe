# tic tac toe

import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def winCondition(inds, grid):
	test = 0
	for i in range(len(inds)):
		test = test + grid[inds[i]]  

	if test == len(inds):
		return 1
	if test == -1 * len(inds):
		return -1
	else:
		return 0


def checkAll(grid):
	indices = np.array([[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])
	#print(indices)
	#print(indices[0,:])
	for x in range(len(indices[:,0])):
		w = winCondition(indices[x,:], grid)
		if w == 1:
			#print("Player 1 wins!")
			return 1
		if w == -1:
			#print("Player 2 wins!")
			return -1
			
	return 0
	

def printGrid(grid):
	gridr = grid.reshape(3,3)
	print(gridr)
	gridx_ = np.array([['X', 'X', 'X'],['X', 'X', 'X'],['X', 'X', 'X']])
	for i in range(3):
		for j in range(3):
			if gridr[i,j] == 1:
				gridx_[i,j] = 'O'
			if gridr[i,j] == -1:
				gridx_[i,j] == 'X'
			if gridr[i,j] == 0:
				gridx_[i,j] = i*3+j

	print(gridx_)


def playerTurn(grid,num):
	"""
	The player's turn.
	Arguments:
	grid = tic tac toe grid
	num = player number (1 or 2)

	returns updated grid
	"""

	print("Player", num)
	check = 0
	if num == 1:
		# Player 1
		while check == 0:
			# Ensure player doesn't try to overwrite a previous play.
			x = int(input("Place an O: "))
			if grid[x] == 0:
				check = 1
				break
		
		# Update grid at player 1's chosen location.
		grid[x] = 1
		return grid


	if num == 2:
		# Player 2
		while check == 0:
			# Ensure player doesn't try to overwrite a previous play.
			x = int(input("Place an X: "))
			if grid[x] == 0:
				check = 1
				break

		# Update grid at player 2's chosen location.
		grid[x] = -1
		return grid


def randomCornerPlay(grid):
	""" Computer play at random corner"""

	check = 0
	while check < 8:
		# Ensure computer doesn't try to overwrite a previous play.
		y = int(random.randint(0,4))
		if y == 0:
			x = 0
		elif y == 1:
			x = 2
		elif y == 2:
			x = 6
		elif y == 3:
			x = 8
		
		if grid[x] == 0:
			return x
		else:
			check = check + 1

	return -1


def randomPlay(grid):
	"""Computer random play"""

	check = 0
	while check == 0:
		# Ensure computer doesn't try to overwrite a previous play.
		x = int(random.randint(0,9))
		if grid[x] == 0:
			check = 1
			break
		
	return x


def computerFindWin(grid, num):
	grid_c = grid # Computer's attempts
	computerNum = 1 - 2*(num-1) # 1 for player 1, -1 for player 2.
	for x in range(9):
		if grid[x] == 0:
			grid_c[x] = computerNum
			win_c = checkAll(grid_c)
			if win_c == computerNum:
				# if the computer wins by making that play
				grid_c[x] = computerNum
				return grid_c
			else:
				grid_c[x] = 0
				grid[x] = 0
	return grid


def computerStopPlayerWin(grid, num):
	grid_p = grid # Computer's simulation of player's next move
	computerNum = 1 - 2*(num-1)
	playerNum = -1*(1 - 2*(num-1))
	for x in range(9):
		if grid[x] == 0:
			grid_p[x] = playerNum
			win_p = checkAll(grid_p)
			if win_p == playerNum:
				# if player would win by moving here, computer must move here to stop them
				grid_p[x] = computerNum
				return grid_p
			else:
				grid_p[x] = 0
				grid[x] = 0
	return grid


def computerPlay(grid, num):
	"""
	Primitive AI written by me
	"""
	
	
	print("Computer turn")
	# Initialise values / arrays.
	computerNum = 1 - 2*(num-1) # 1 for player 1; -1 for player 2.
	grid_original = np.zeros(9)
	zero_grid = np.zeros(9)
	# Store the original grid in a separate memory location, just to make sure it doesn't get overwritten.
	for i in range(len(grid)):
		grid_original[i] = grid[i]
	
	
	# Algorithm for computer decide what move to play.

	# Occupy the middle square if unoccupied.
	if grid[4] == 0:
		grid[4] = computerNum
		print("Computer went to middle")
		return grid

	
	grid_c = computerFindWin(grid, num)
	if (grid_c == grid_original).all():
		print("Computer did not find a win")
	else:
		print("Computer found a win")
		return grid_c

	grid_p = computerStopPlayerWin(grid, num)
	#print("grid_p")
	#printGrid(grid_p)
	if (grid_p == grid_original).all():
		print("Computer did not find a way for player to win on their next move")
	else:
		print("Computer found a way to stop player from winning on their next move")
		return grid_p


	# If none was better at its search depth, play a random move.
	print("Computer played into a random corner")
	x = int(randomCornerPlay(grid))
	if x == -1:
		print("Computer played a random move")	
		x = int(randomPlay(grid))
	
	grid[x] = computerNum
	return grid


# The main part of the program
def main(player = 0):
	if player == 0:
		a = 0 
		while a == 0:
			player = int(input("Would you like to go first [1] or second [2]? "))
			if player == 1 or player == 2 or player == -1:
				a = 1
				playerWin = 1 - (player-1)*2
				break
	else:
		playerWin = 1
	grid = np.array([0,0,0,0,0,0,0,0,0])
	count = 0
	win = 0
	while win == 0:
		# Loop until one player wins.
		printGrid(grid)
		if count == 9:
			print('--------------')
			print("Draw!")
			print('--------------')
			return 0
			
		if count > 4:
			win = checkAll(grid)
			if win == playerWin:
				print('--------------')
				print("Player wins!")
				print('--------------')
				return 1
			if win == -1*playerWin:
				print('--------------')
				print("Computer wins!")
				print('--------------')
				return -1

		
		turn = 1 + count%2 # Whose turn it is to play.
		if player == turn:
			grid = playerTurn(grid, turn)
		else:
			grid = computerPlay(grid, turn)
		count = count + 1
		

#main(playnum)


def test1():
	testgrid = np.array([0,1,0,-1,1,0,-1,0,0])
	printGrid(testgrid)
	grid2 = computerPlay(testgrid,1)
	printGrid(grid2)

	solution = np.array([0,1,0,-1,1,0,-1,1,0])
	if (solution == grid2).all():
		print("PASS")
	else:
		print("FAIL")

#test1()

condition = 0
while condition == 0:
	mode = int(input("Play mode [0] or test mode [1]?"))
	if mode == 0 or mode == 1:
		condition = 1
		break

if mode == 0:
	main()
elif mode == 1:
	import sys
	file = open('tictactoe.txt', 'a')
	sys.stdout = file

	N = 10000
	results = np.zeros(N)
	for i in range(N):
		results[i] = main(-1)

	file.close()
	# Plot results and save figure
	plt.plot(results)
	plt.savefig('tictactoe.png')
	plt.show()

#print(win)