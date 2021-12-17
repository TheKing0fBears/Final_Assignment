import pygame
import math
from queue import PriorityQueue

SIZE = 1000#size of display
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Pathfinding assignment")

#colors for the display
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)

class Node:
  def __init__(self,row,col,width,total_rows)
    self.row = row#simplification of variables for later use
    self.col = col
    self.x=row*width
    self.y=col*width
    self.color=BLACK
    self.neighbors = []
    self.width = width
    self.total_rows = total_rows
    
  
  #functions for changes in state of each node
  def get_position(self):
    return self.row,self.col
  
  def bad_path(self):
    return self.color == RED
  
  def good_path(self):
    return self.color == GREEN

  def obsticle(self):
	return self.color == BLUE
  
  def starting(self):
    return self.color == WHITE
  
  def ending(self):
    return self.color ==WHITE
  
  def reset_node(self):
    return self.color == BLACK
  
  def make_start(self):
		self.color = WHITE
    
  def make_end(self):
		self.color = WHITE

	def make_bad(self):
		self.color = RED

	def make_good(self):
		self.color = GREEN

	def make_obsticle(self):
		self.color = BLUE
    
	def make_path(self):
		self.color = YELLOW

 #function to draw rectangles on screen
  def draw(window,self.color,(self.x,self.y,self.width,self.width))
  
  #function to update neighboring nodes
  def update(self,grid):
	self.neighbors = []
	if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].obsticle(): #look down
	if self.row > 0 and not grid[self.row - 1][self.col].obsticle(): # look up
		self.neighbors.append(grid[self.row - 1][self.col])
	if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].obsticle(): #look right
		self.neighbors.append(grid[self.row][self.col + 1])
	if self.col > 0 and not grid[self.row][self.col - 1].obsticle(): # look left
		self.neighbors.append(grid[self.row][self.col - 1])
			
	def __1t__(self,other):
		return False
	
def dist(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return abs(x1-x2)+abs(y1-y2)

def path(old,current,draw):
	while current in old:
		current=old[current]
		current.make_path()
		draw()

def astar(draw,grid,start,ending):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0,count,start))
	old = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = dist(start.get_pos(), ending.get_pos())
	
	open_set_hash = {start}
	
	while not open_set.empty()
		for event in pygame.event.get()[2]
			if event.type == pygame.QUIT:
				pygame.quit()
			
			current = open_set.get()[2]
			open_set_hash.remove(current)
			
			if current == ending:
				path(old,ending,draw)
				ending.make_end()
			
	
	
	
