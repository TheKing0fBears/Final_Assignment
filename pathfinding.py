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
  
  def is_closed(self):
    return self.color == RED
  
  def is_open(self):
    return self.color == GREEN

  def is_barrier(self):
	return self.color == BLUE
  
  def is_start(self):
    return self.color == WHITE
  
  def is_end(self):
    return self.color ==WHITE
  
  def reset(self):
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
  def update_neighbors(self,grid):
	self.neighbors = []
	if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_barrier(): #look down
	if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # look up
		self.neighbors.append(grid[self.row - 1][self.col])
	if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #look right
		self.neighbors.append(grid[self.row][self.col + 1])
	if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # look left
		self.neighbors.append(grid[self.row][self.col - 1])
			
	def __1t__(self,other):
		return False
	
  def h(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return abs(x1-x2)+abs(y1-y2)

  def construct_path(old,current,draw):
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
				return True
			
			for neighbor in current.neighbors:
				temp_g_score = g_score[current] + 1
				
				if temp_g_score < g_score[neighbor]:
					came_from[neighbor] = current
					g_score[neighbor] = temp_g_score
					f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), ending.get_pos())
					
					if neighbor not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbor], count, neighbor))
						open_set_hash.add(neighbor)
						neighbor.make_good()
			draw()
			
			if current !=start:
				current.make_bad()
		
		return False

  def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


  def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


  def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


  def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col
	
  def main(win, width):
	ROWS = 128
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)	
	pygame.quit()
main(WIN,SIZE)
