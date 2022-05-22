import numpy as np

# Tic-Tac-Toe Game
# Ashutosh Tiwari
#
# B is the game board
# X -> 1, O -> -1, empty-> 0


def display(B):
	for i in range(3):
		print("\t\t", end = '')
		for j in range(3):
			if(B[i][j]==1):
				print("X", end = '')
			elif(B[i][j]==-1):
				print("O", end = '')
			elif(B[i][j]==0):
				print(" ", end = '')
			if(j<2):
				print(" | ", end = '')
			else:
				print("")
		if(i<2):
			print("\t\t----------")
	print("\n")


def is_possible(B):
	for i in range(3):
		for j in range(3):
			if(B[i][j]==0):
				return True
	return False

def is_finished(B):
	# return 1 if X won, 0 if tie, -1 if O won, 2 if move is possible
	for i in range(3):
		if(B[i][0]):
			if(B[i][0]==B[i][1]  and  B[i][1]==B[i][2]):
				return B[i][0]			# return the element which won

	for j in range(3):
		if(B[0][j]):
			if(B[0][j]==B[1][j]  and  B[1][j]==B[2][j]):
				return B[0][j]
	
	if(B[0][0]!=0  and  B[0][0]==B[1][1]  and  B[1][1]==B[2][2]):
		return B[0][0]
	elif(B[0][2]!=0  and  B[0][2]==B[1][1]  and  B[1][1]==B[2][0]):
		return B[0][2]
	#nobody won
	if(is_possible(B)==False):
		return 0 		#tie

	return 2  #move is possible


#computer is X
def max(B, alpha, beta):

	res = is_finished(B)

	if(res == 1):	#X won
		return (1, -1, -1)		#no move is required
	elif(res == -1):
		return (-1, -1, -1)
	elif(res == 0):
		return (0, -1, -1)

	max_v = -2
	px = -1
	py = -1

	for i in range(3):
		for j in range (3):
			if(B[i][j]==0):
				B[i][j] = 1;	#place X at empty cell and calculate min
				(m, x, y) = min(B, alpha, beta)
				if(m > max_v):
					max_v = m
					px = i
					py = j
				B[i][j] = 0

				if(max_v > alpha):
					alpha = max_v

				if(max_v >= beta):
					return (max_v, px, py)

	return (max_v, px, py)




def min(B, alpha, beta):

	res = is_finished(B)

	if(res == 1):	#X won
		return (1, -1, -1)
	elif(res == -1):
		return (-1, -1, -1)
	elif(res == 0):
		return (0, -1, -1)

	min_v = 2
	px = -1
	py = -1

	for i in range(3):
		for j in range(3):
			if(B[i][j]==0):
				B[i][j] = -1;			#placeing O
				(m, x, y) = max(B, alpha, beta)
				if(m < min_v):
					min_v = m
					px = i
					py = j
				B[i][j] = 0

				if(min_v < beta):
					beta = min_v

				if(min_v < alpha):
					return(min_v, px, py)

	return (min_v, px, py)



def play(B, turn):
	#turn = 'O'			# starting the game with turn of X (computer)
	dict = {1 : (0,0), 2 : (0,1), 3 : (0,2), 4 : (1,0), 5 : (1,1), 6 : (1,2), 7 : (2,0), 8 : (2,1), 9 : (2,2) }

	while(True):
		res = is_finished(B)

		if(res == 1):
			display(B)
			print("      Game Over\nResult: Computer Won!")
			return
		elif(res == -1):
			display(B)
			print("   Game Over\nResult: You Won!")
			return
		elif(res == 0):
			display(B)
			print(" Game Over\nResult: Tie!")
			return

		if(turn == 'X'):
			(m, x, y) = max(B, -2, 2)			#alpha = -inf,  beta = +inf
			B[x][y] = 1
			turn = 'O'
		else:
			display(B)
			p = int(input("Your turn : "))
			while(p<1  or  p>9):
				print("Invalid Move. Please enter a valid number")
				p = int(input("Your turn : "))
			(x, y) = dict[p]
			while(B[x][y] != 0 ):
				print("Invalid Move. Please enter a valid cell")
				p = int(input("Your turn : "))
				while(p<1  or  p>9):
					print("Invalid Move. Please enter a valid number")
					p = int(input("Your turn : "))
				(x, y) = dict[p]
			B[x][y] = -1
			turn = 'X'




#Main
B = np.zeros((3, 3), dtype=int)

print("\t\tTic-Tac-Toe\n")

t = int(input("Do you want first turn?  "))
if (t == 1):
	turn = 'O'
else:
	turn = 'X'
print("\n")

play(B, turn) 