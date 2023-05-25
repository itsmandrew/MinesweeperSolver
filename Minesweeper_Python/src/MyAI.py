# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action


class Board:

	FLAG = "X"
	UNCOVERED_TILE = "."

	def __init__(self, rows, columns) -> None:
		self.board = [["." for j in range(columns)] for i in range(rows)]
		self.columns = columns
		self.rows = rows

	def is_legal(self, x, y) -> bool:
		if 0 <= x < self.columns and 0 <= y <= self.rows:
			return True
		return False

	def get_value(self, x, y) -> int:
		if self.is_legal(x, y):
			return self.board[y][x]
		
		return -1
	
	def set_value(self, x, y, char) -> None:
		if self.is_legal(x, y):
			self.board[y][x] = char
			return True
		return False

	def display(self):
		print("===" * (self.rows + 1), "[board]")
		for i in range(self.rows - 1, -1, -1):
			print(i + 1, end=" | ")
			for j in range(self.columns):
				print(self.board[i][j], end="  ")
			print()
		print("   ", end="")
		for i in range(self.columns):
			print(" - ", end="")
		print()
		print("    ", end="")
		for i in range(self.columns):
			print(i + 1, end="  ")
		print()



class MyAI( AI ):

	# CODES FOR THE FOUR STATES
	LEAVE = 0
	UNCOVER = 1
	FLAG = 2
	UNFLAG = 3

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
		

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		self.board = Board(rowDimension, colDimension)
		self.matrix = [[-1 for _ in range(colDimension)] for _ in range(rowDimension)]

		self.totalMines = totalMines
		self.frontire = []
		self.frontire.append([startX,startY])
		self.last = -1
		self.bomb = -1

		self.colDimension = colDimension
		self.rowDimension = rowDimension
		self.visited = set()


		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		if self.last != -1:
			self.matrix[self.last[0]][self.last[1]] = number
			self.board.set_value(self.last[0], self.last[1], number)

			if (number == 0):
				#x-axis for surrounding last, I just subtracted 1 from it each time
				for x in range(3):
					#checks if the x axis of each side would be over or under max
					if self.last[0]+(x-1) >=0 and self.last[0]+(x-1) <=4:
						#y axis, also just subtracted one
						for y in range(3):
							if self.last[1]+(y-1) >=0 and self.last[1]+(y-1) <=4:
								if self.matrix[self.last[0]+(x-1)] [self.last[1]+(y-1)] == -1 and (self.last[0]+(x-1), self.last[1]+(y-1)) not in self.visited:
									#if the square adjacent to last is on the board and not already turned, add it to frontire
									self.frontire.append([self.last[0]+(x-1), self.last[1]+(y-1)])
									self.visited.add(tuple([self.last[0]+(x-1), self.last[1]+(y-1)]))
			#update surroundings in matrix
		
		#printing, so we can see what it looks like
		#self.board.display()

		if len(self.frontire) == 0:
			#all obvious white space cleared so now have to deal with edge cases

			#### CONTINUING THE SECOND LAYER !!!!
			new_frontier = [ [i, j] for j in range(self.colDimension) for i in range(self.rowDimension) if (self.board.get_value(i, j) != 0 and self.board.get_value(i, j) != ".")]
			#print(new_frontier)
			
			return Action(AI.Action.LEAVE)
		
		else:
			self.last = self.frontire.pop()
			self.visited.add(tuple(self.last))
			#print(self.frontire)
			return Action(AI.Action.UNCOVER, self.last[0], self.last[1])
		

		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
