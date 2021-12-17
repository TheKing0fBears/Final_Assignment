import pygame#using pygame library for graphical display
import math
from queue import PriorityQueue

WIDTH = 1000#size of the screen
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding_Final_Kyle")

#colors for the display
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREY = (128, 128, 128)


#class for the different spots on the grid
class Spot:
	#simplification of variables for later use
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = BLACK
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):#gets current position of a spot on grid
		return self.row, self.col

	def is_closed(self):#checks to see if a spot is closed
		return self.color == RED

	def is_open(self):#checks to see if a spot is open
		return self.color == GREEN

	def is_barrier(self):#checks to see if a spot is a barrier
		return self.color == WHITE

	def is_start(self):#the start of the pathing
		return self.color == BLUE

	def is_end(self):#the end of the pathing
		return self.color == BLUE

	def reset(self):#reset the grid
		self.color = BLACK

	def make_start(self):#creates the start of the path
		self.color = BLUE

	def make_closed(self):#closes a spot for testing
		self.color = RED

	def make_open(self):#means that the spot is open to be tested
		self.color = GREEN

	def make_barrier(self):#creates an obsticle for the path to move around
		self.color = WHITE

	def make_end(self):#makes the ending point
		self.color = BLUE

	def make_path(self):#final path
		self.color = YELLOW

	def draw(self, win):#draws a spot on the grid
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

		
	##This function will update neighboring spots##	
	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #check if you can move down
			self.neighbors.append(grid[self.row + 1][self.col])#add to neighbors

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # check if you can move up
			self.neighbors.append(grid[self.row - 1][self.col])#add to neighbors

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # check if you can move right
			self.neighbors.append(grid[self.row][self.col + 1])#add to neighbors

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # check if you can move left
			self.neighbors.append(grid[self.row][self.col - 1])#add to neighbors

	##--this function checks to see if the spot is less than another spot
	def __lt__(self, other):
		return False

##This function checks the distance between two points witha heuristic algorithm##
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

##This function will recreate the shortest path needed to reach the end goal##
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

##This function is the algorithm for an a* pathfinding system
def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}#start at infinity because nothing is there
	g_score[start] = 0#initialize g score at 0
	f_score = {spot: float("inf") for row in grid for spot in row}#start at infinity because nothing is there
	f_score[start] = h(start.get_pos(), end.get_pos())#initialize h score with the positions of the end and start

	open_set_hash = {start}#make set for the priority queue to keep track of items

	while not open_set.empty():#checks to see if the open set is empty suggesting that the path doesnt exist if the end isnt found
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()#quit the program

		current = open_set.get()[2]#start spot
		open_set_hash.remove(current)#remove the current spot from the hash to get rid of residue

		if current == end:
			reconstruct_path(came_from, end, draw)#create the path to the end
			end.make_end()#make the end the correct color again
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:#if better path is found than neighbor
				came_from[neighbor] = current 
				g_score[neighbor] = temp_g_score 
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:#add neighbor into queue
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()#open the next neighbor to be checked

		draw()

		if current != start:#close if not the start or a neighbor
			current.make_closed()

	return False

##this function will create the grid##
def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)#create spot object
			grid[i].append(spot)#add spot into grid

	return grid


##This function will actually draw the grid into the pygame window##
def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))#draws line on the horizontal for each row
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))#draws line on vertical for each row

#This function is used to draw spots
def draw(win, grid, rows, width):
	win.fill(BLACK)#fill window 

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


#this function returns the coordinate of the clicked object
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col


def main(win, width):
	ROWS = 100
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: #left click
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

			elif pygame.mouse.get_pressed()[2]: #right click
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:#when space is pressed start the program
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				
				if event.key == pygame.K_c:#when c is pressed reset the program
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

#run program
main(WIN, WIDTH)
