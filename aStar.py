import pygame as gfx

class Posistion: 
	def __init__(self, x, y)
		self.x = x
		self.y = y
	def Equals(self, other)
		return True if (self.x == other.x and self.y == other.y) else False 
		
class Node:
	def __init__(self, x, y):
		self.parent = None	# null until assigned elsewhere
		self.color = (255,255,255)	# default white
		self.width  = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) * x + self.margin
		self.top  = (self.margin + self.height) * y + self.margin
		self.walkable = True # default to True Until changed elsewhere
		
		self.pos = (x,y)
		self.x = ( 5 + self.height) * x + 5
		self.y = ( 5 + self.height) * y + 5
		self.screenPos = (x,y)
		
		self.g = None	# the movement cost to move from the starting point to a given square on the grid, following the path generated to get there
		self.h = None	# the estimated movement cost to move from that given square on the grid to the final destination
		self.f = getF() # G+H
		
	def 
	
	def draw(self, screen, color):
		margin = self.margin
		color = (0, 0, 255) if (self.walkable) else (255, 0, 0)
		gfx.draw.rect(screen, color (self.left, self.top, self.width, self.height))
		
	def setWalk(self, walkable):
		self.walkable = walkable
	def getF(self):
		return self.h + self.g
	def setH(self, value):
		self.h = value
	def setG(self, value):
		self.g = value
	
class Astar:
	def __init__(self, SearchSpace, Start, Goal, Row, Column):	# Everything a young pathing program needs
		self.OPEN = []			# Array of all Open Nodes
		self.CLOSED = []		# Array of all Closed Nodes	# 
		self.SearchGrid = {}	# My Dict of Nodes
		OPEN.append(Start)		# Add Starting node to open to start process
		SetHValues()
		
	def SetHValues(self):
		for n in (SearchSpace)
			xh = Goal.x - n.x
			yh = Goal.y - n.y
			n.setH(xh + yh)
	
	def SetUpGrid(self):	# Return Array of Nodes
		for x in (Row):
			for y in (Column):
				n = Node(x,y)
				r = random()%2
				n.walkable = True if r == 0 else False
				self.SearchGrid[x,y] = n)
		
	
	def Run(self):
		while not Goal in self.OPEN:
			current = self.LowestF(self.OPEN)
			GetAdjacent(current)
	
	def LowestF(self, Nodes):	# Find cheapest F of the possible steps
		Nodes.sort(key = lambda x: x.f)
		return Nodes[0]
		
	def GetAdjacent(self, node):	# Get all valid nodes Adjacent to a specified node # Return the Array of Nodes
		CLOSED.append(node)
		OPEN.remove(node)
		# Top Left 		# -x +y
		if (SearchGrid and SearchGrid[node.posistion.x-1, node.posistion.y+1].walkable and SearchGrid[node.posistion.x-1, node.posistion.y+1] not in  OPEN):
			OPEN.append(SearchGrid[node.posistion.x-1, node.posistion.y+1])
			SearchGrid[node.posistion.x-1, node.posistion.y+1].parent = node
		# Top Middle 	#  x +y
		# Top Right 	# +x +y
		# Left 			# -x  y
		# Right 		# +x  y
		# Bottom Left 	# -x -y
		# Bottom Middle #  x -y
		# Bottom Right 	# +x -y
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		