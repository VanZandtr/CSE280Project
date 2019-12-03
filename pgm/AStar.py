'''
A* Implementation using a Priority Queue to get the lowest cost nodes

Converts a 2D IntegerArray into a NodeArray
Pathfind through NodeArray and returns the node from the end point or None if no path found
To find path, access node.parent until node.parent == None

Coordinate scheme is board[y][x]

Created by Matthew Levy

'''

import sys

'''
0 - Pathway
1 - Wall
'''

board = [
	[3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
]

class Node():
	def __init__(self, point, g, h, parent=None):
		self.point  = point
		self.g      = g
		self.h      = h
		self.parent = parent
	def getCost(self):
		return self.g + self.h
	def __repr__(self):
		return 'Point: {}\tCost: {}\tParent: {}\n'.format(self.point, self.getCost(), self.parent.point)

class PriorityQueue():
	def __init__(self):
		self.__queue = []
	def size(self):
		return len(self.__queue)
	def insert(self, value):
		self.__queue.append(value)
	def remove(self):
		if len(self.__queue) == 0: return None
		
		smallest = 0
		for i in range(1, len(self.__queue)):
			if self.__queue[i].getCost() < self.__queue[smallest].getCost():
				smallest = i
		
		ret = self.__queue[smallest]
		del self.__queue[smallest]
		
		return ret	
	def __repr__(self):
		ret = ''
		for entry in self.__queue:
			ret += 'Point: {}\tCode: {}\n'.format(entry.point, entry.getCost())
		return ret

class AStar():
	NORMAL_COST  = 10
	DIAGNOL_COST = 14
	
	def __init__(self, board):
		self.__board     = board
		self.__height    = len(board)
		self.__width     = len(board[0])
		self.__nodeBoard = self.__createNodeBoard()
	
	def __createNodeBoard(self):
		nodeBoard = []
		for i in range(self.__height):
			nodeRow = []
			for j in range(self.__width):
				# maxint == infinity
				nodeRow.append(Node([i, j], sys.maxsize, sys.maxsize))
			nodeBoard.append(nodeRow)
		return nodeBoard
	
	def __distance(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])
	
	def __cost(self, end, current_cost, point):
		return (current_cost + 1) + self.__distance(end, point)
	
	def __isDiagnol(self, current_point, next_point):
		if current_point[0] != next_point[0] and current_point[1] != next_point[1]:
			return True
		return False
	
	def __neighbors(self, node):
		points = []
		points.append([node[0] - 1, node[1] - 1])
		points.append([node[0] - 1, node[1]    ])
		points.append([node[0] - 1, node[1] + 1])
		points.append([node[0],     node[1] - 1])
		points.append([node[0],     node[1] + 1])
		points.append([node[0] + 1, node[1] - 1])
		points.append([node[0] + 1, node[1]    ])
		points.append([node[0] + 1, node[1] + 1])
		
		ret = []
		for point in points:
			if point[0] < 0 or point[0] >= self.__height or point[1] < 0 or point[1] >= self.__width or self.__board[point[0]][point[1]] == 1:
				continue
			ret.append(self.__nodeBoard[point[0]][point[1]])
		
		return ret
	
	def findPath(self, start, end):
		frontier = PriorityQueue()
		node = Node(start, 0, self.__distance(start, end))
		frontier.insert(node)
		
		close_list = []
		current    = None
		while frontier.size() > 0:
			current = frontier.remove()
			if current.point[0] == end[0] and current.point[1] == end[1]:
				break
			
			for neighbor in self.__neighbors(current.point):
				# Get associated node
				point = neighbor.point
				
				h = self.__distance(point, end)
				g = current.g
				if self.__isDiagnol(current.point, point):
					g += self.DIAGNOL_COST
				else:
					g += self.NORMAL_COST
				
				new_cost = g + h
				
				if neighbor.getCost() > new_cost or neighbor not in close_list:
					neighbor.g      = g
					neighbor.h      = h
					neighbor.parent = current
					
					close_list.append(neighbor)
					frontier.insert(neighbor)
		if current.point != end:
			current = None
		return current

def printBoard(board, end_node, start, end):
	# Create a copy
	board = board[:]
	
	points = []
	while end_node:
		points.append(end_node.point)
		end_node = end_node.parent
	points.reverse()
	
	import time
	import os
	for point in points:
		os.system("clear")
		board[point[0]][point[1]] = 2
		
		board[start[0]][start[1]] = 3
		board[end[0]][end[1]]     = 3
		
		__printBoard(board)
		time.sleep(1)
	

def __printBoard(board):
	sys.stdout.write('-'*(len(board) + 2) + '\n')
	for row in board:
		sys.stdout.write('|')
		for col in row:
			if col == 0:
				sys.stdout.write(' ')
			elif col == 1:
				sys.stdout.write('#')
			elif col == 2:
				sys.stdout.write('^')
			elif col == 3:
				sys.stdout.write('@')
		sys.stdout.write('|\n')

def main():
	# Find path on board
	start = []
	end   = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 3:
				if start == []:
					start.append(i)
					start.append(j)
				elif end == []:
					end.append(i)
					end.append(j)
	
	astar = AStar(board)
	node = astar.findPath(start, end)
	
	inp = raw_input('Display Path? (y/N)')
	if inp == 'y' or inp == 'Y':
		printBoard(board, node, start, end)
	
	print('Path:')
	current = node
	path = []
	path_cost = 0
	while current:
		print('\tPoint: [{:0>2d}, {:0>2d}] | G: {:0>4d} | H: {:0>4d} | Cost: {:0>4d}'.format(current.point[0], current.point[1], current.g, current.h, current.getCost()))
		path.append(current.point)
		path_cost += current.getCost()
		current = current.parent
	print('Path Cost: {}'.format(path_cost))

if __name__ == '__main__':
    main()
