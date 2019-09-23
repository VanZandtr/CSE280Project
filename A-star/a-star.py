'''
A* Implementation using a Priority Queue to get the lowest cost nodes

Converts a 2D IntegerArray into a NodeArray
Pathfind through NodeArray and returns the node from the end point or None if no path found
To find path, access node.parent until node.parent == None

Coordinate scheme is board[y][x]
'''

import sys
import os
import time
from MapParser import *

'''
0 - Pathway
1 - Wall
'''

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return '[{}, {}]'.format(self.x, self.y)
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

class Node():
	def __init__(self, point, g, h, parent=None):
		self.point  = point
		self.g      = g
		self.h      = h
		self.parent = parent
	def getCost(self):
		return self.g + self.h
	def __repr__(self):
		return 'Point: {}\tCost: {}\tParent: {}\n'.format(self.point, self.getCost(), self.parent.point if self.parent else 'N/A')

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
				nodeRow.append(Node(Point(j, i), sys.maxint, sys.maxint))
			nodeBoard.append(nodeRow)
		return nodeBoard
	
	def __distance(self, a, b):
		dx = abs(a.x - b.x)
		dy = abs(a.y - b.y)
		return dx + dy
	
	def __cost(self, end, current_cost, point):
		return (current_cost + 1) + self.__distance(point, end)
	
	def __neighbors(self, node):
		points = []
		points.append(Point(node.x - 1, node.y - 1))
		points.append(Point(node.x - 1, node.y    ))
		points.append(Point(node.x - 1, node.y + 1))
		points.append(Point(node.x,     node.y - 1))
		points.append(Point(node.x,     node.y + 1))
		points.append(Point(node.x + 1, node.y - 1))
		points.append(Point(node.x + 1, node.y    ))
		points.append(Point(node.x + 1, node.y + 1))
		
		ret = []
		for point in points:
			if point.y < 0 or point.y >= self.__height or point.x < 0 or point.x >= self.__width or self.__board[point.y][point.x] > 0:
				continue
			ret.append(self.__nodeBoard[point.y][point.x])
		
		return ret
	
	def findPath(self, start, end):
		frontier = PriorityQueue()
		node = Node(start, 0, self.__distance(start, end))
		frontier.insert(node)
		
		close_list = []
		current    = None
		while frontier.size() > 0:
			current = frontier.remove()
			if current.point == end:
				break
			
			for neighbor in self.__neighbors(current.point):
				if neighbor.point in close_list: continue
				
				# Get associated node
				point = neighbor.point
				
				h = self.__distance(point, end)
				# TODO: Won't work if g increments
				g = current.g# + 1
				
				new_cost = g + h
				if neighbor.getCost() > new_cost or neighbor.point not in close_list:
					neighbor.g      = g
					neighbor.h      = h
					neighbor.parent = current
					
					close_list.append(neighbor.point)
					frontier.insert(neighbor)
		return current if current.point == end else None

def main(map_file, start_pt, end_pt, out_file='map.pgm', line_width=10):
	board = Map2Array(map_file)
	
	# Find path on board
	#        x     y
#	start = Point(592, 120)
#	end   = Point(540, 1524)
	s_pt = start_pt.split(',')
	e_pt = end_pt.split(',')
	start = Point(int(s_pt[0]), int(s_pt[1]))
	end   = Point(int(e_pt[0]), int(e_pt[1]))

	start_time = time.time()
	astar = AStar(board)
	node = astar.findPath(start, end)
	
	current = node
	path = []
	while current:
	#	print '\tPoint: [{:0>2d}, {:0>2d}] | G: {:0>4d} | H: {:0>4d} | Cost: {:0>4d}'.format(current.point.x, current.point.y, current.g, current.h, current.getCost())
		pt = current.point
		
		for i in range(line_width):
			for j in range(line_width):
				board[pt.y + i][pt.x + j] = 125

		path.append(pt)
		current = current.parent
		
	Array2Map(board, out_file)
	PGM2PNG(out_file)
	os.remove(out_file)
	
	elapsed_time = time.time() - start_time
	print 'Elapsed Time: {} seconds'.format(elapsed_time)

if __name__ == '__main__':
	main(sys.argv[1], out_file=sys.argv[2], start_pt=sys.argv[3], end_pt=sys.argv[4])
