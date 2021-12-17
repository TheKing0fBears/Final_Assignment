import pygame
import math
from queue import PriorityQueue

SIZE = 1000#size of display
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Pathfinding assignment")

#colors for the display
BLACK = (0,0,0)
RED = (255,0,0)

class Node:
  def __init__(self,row,col,width,total_rows)
    self.row = row#simplification of variables for later use
    self.col = col
    self.x=row*width
    self.y=col.width
    self.color=BLACK
    self.neighbors = []
    self.width = width
    self.total_rows = total_rows
    
  def get_position(self):
    return self.row,self.col
  
  def bad_path
    return self.color == RED
