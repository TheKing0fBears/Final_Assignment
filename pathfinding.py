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
  def 
