'''
	Tic-tac-toe - Master
	Author: adri711
	Language: Python
	Written on: 28/07/2020
'''
import sys, pygame
from time import time
from dataset import load, insert_into_dataset
from sklearn import tree
import numpy as np
import random


class gui_button():
	elements = []
	def __init__(self, button_identificator, button_text, text_size,width, height, x, y, color, hovercolor,frame, triggered_event,*args):
		self.trigger_function = triggered_event
		self.arguments = args
		self.coords = [x,y]
		self.size = [width, height]
		self.text = str(button_text)
		self.text_size = text_size
		self.name = str(button_identificator)
		self.color = color
		self.hover_color = hovercolor
		self.status = True #enabled/disabled
		self.frame = frame
		print(self.name + " has been created at x,y: " + str(self.coords[0]) + "," + str(self.coords[1]) + " width, height: " + str(self.size[0]) + "," + str(self.size[1]))
		print("assigned event: " + triggered_event.__name__)
		gui_button.elements.append(self)
		del self
	def toggle(self, new_status):
		for element in gui_button.elements:
			if element == self:
				self.status = new_status
	def mousehover(self):
		x, y = pygame.mouse.get_pos()
		if x >= self.coords[0] and x <= self.coords[0] + self.size[0] and y >= self.coords[1] and y<= self.coords[1] + self.size[1]:
			return True
		return False

features, labels = load()
def test_func(text):
	print(text)

adri713 = tree.DecisionTreeClassifier()
adri713.fit(features,labels)

pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')

pygame.display.set_icon(pygame.image.load('icon.png'))
#
pvp = 0
pvai = 1
training = 2

game_mode = pvai
game_inmenu = 0
game_inprocess = 1
game_over = 2
game_intraining = 3
end_time = time()
winner = 0

game_state = game_inmenu

SCREEN_HEIGHT = 420
SCREEN_WIDTH = 420

game_field_x = 62
game_field_y = 62

button_height = 47
button_width = 132

moves = 0
x69 = 1
o = 2

pvp_button_coords = [ int(SCREEN_WIDTH / 2 - button_width / 2), int(SCREEN_HEIGHT / 2 - button_height / 2)]
pvai_button_coords = [ int(SCREEN_WIDTH / 2 - button_width / 2), int(SCREEN_HEIGHT / 2 - button_height / 2) + button_height + 10 ]
training_button_coords = [ int(SCREEN_WIDTH / 2 - button_width / 2), int(SCREEN_HEIGHT / 2 - button_height / 2) + button_height * 2 + 20]

pvp_id = "pvp_btn"
pvai_id = "pvai_btn"
pvt_id = "pvt_btn"
back_id = 'back_btn'
train_id = 'train_btn'
field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
last_move = ['', 0, 0]
#colors 
white = 255, 255, 255
black = 0, 0, 0
silver = 192,192,192
darkgrey = 32,32,32
green = 32, 168, 32
red = 168, 32, 32
#
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#
def multiple_char_check(text):
	result = True
	if len(text) != 0 and len(text) != 1:
		last_char = text[0]
		for char in text:
			if char != last_char:
				result = False
				break
			last_char = char
	return result

def start_game(mode):
	global game_mode, game_state, moves, field, winner, features, labels
	game_mode = mode
	if game_mode != training:
		game_state = game_inprocess
		if game_mode == pvai:
			features, labels = load() #Reloading data 
	else:
		game_state = game_intraining
	field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	moves = 0
	winner = ''


def quit_game():
	global game_state
	game_state = game_inmenu

def game_check(game_list):
	final_result = '0'
	for row in game_list:
		result = multiple_char_check(row)
		if result == True and row[0] != 0:
			if row[0] == o:
				return 'o'
			elif row[0] == x69:
				return 'x'
		else:
			final_result = '0'
	for i in range(len(game_list)):
		row = []
		for j in range(len(game_list)):
			row.append(game_list[j][i])
		result = multiple_char_check(row)
		if result == False:
			final_result = '0'
		else:
			if row[0] == o:
				return 'o'
			elif row[0] == x69:
				return 'x'

	row = [game_list[0][0], game_list[1][1], game_list[2][2]] 

	if multiple_char_check(row):
		if row[0] == o:
			return 'o'
		elif row[0] == x69:
			return 'x'
	row = [game_list[0][2], game_list[1][1], game_list[2][0]]
	if multiple_char_check(row):
		if row[0] == o:
			return 'o'
		elif row[0] == x69:
			return 'x'
	return 	final_result

def insert_record():
	global field, last_move

	if last_move[0] == 'o':
		field[last_move[1]][last_move[2]] = 0
		temp = []
		for row in field:
			for item in row:
				temp.append(str(item))

		insert_into_dataset(temp, [last_move[1],  last_move[2]])
	else:
		print("ERROR: You can't save this.")

#Buttons
pvp_button = gui_button(pvp_id, "Player vs Player", 12,  button_width, button_height, pvp_button_coords[0], pvp_button_coords[1], green, red, [game_inmenu], start_game, pvp)
pvai_button = gui_button(pvai_id, "Player vs AI", 12,  button_width, button_height, pvai_button_coords[0], pvai_button_coords[1], green, red, [game_inmenu], start_game, pvai)
pvt_button = gui_button(pvt_id, "Train AI model", 12, button_width, button_height, training_button_coords[0], training_button_coords[1], green, red, [game_inmenu], start_game, training)
back_button = gui_button(back_id, "Go back", 12, 62, 32, SCREEN_WIDTH - 72, 6, green, red, [game_inprocess, game_intraining], quit_game)
train_button = gui_button(train_id, "Save i/o put", 12, 80, 32, SCREEN_WIDTH  - 180, 6, green, red,[game_intraining], insert_record)

while True:
	rectangle_w = (SCREEN_WIDTH-game_field_x) / 3
	rectangle_h = (SCREEN_HEIGHT-game_field_y) / 3
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()

			if game_state == game_inprocess or game_state == game_intraining:
				for i in range(len(field)):
					for z in range(len(field[i])):
						if game_field_x + rectangle_w * z <= x and game_field_x + rectangle_w * z + rectangle_w >= x:
							if game_field_y + rectangle_h * i <= y and game_field_y + rectangle_h * i + rectangle_h >= y:
								if game_mode != training:
									if field[i][z] == 0:
										field[i][z] = x69
										moves+=1
										if game_mode == pvp:
											if moves % 2 == 0:
												field[i][z] = o
										elif game_mode == pvai:
											if game_check(field) != 'x':
												temp_list = []
												for row in field:
													temp_list.extend(row)
												max_count = 5
												count = 0
												result = adri713.predict([temp_list])
												while field[result[0][0]][result[0][1]] != 0 and moves < 8:
													xc = random.randint(0,2)
													xy = random.randint(0,2)
													result[0][0], result[0][1] = xc, xy
												if moves < 9:
													field[result[0][0]][result[0][1]] = o
													moves+=1
										result=game_check(field)
										if result == 'x' or result == 'o':
											winner = result
											game_state = game_over
											end_time = time() + 3
										else:
											if moves >= 9:
												game_state = game_over
												end_time = time() + 3
												winner = "It's a tie."
								elif game_mode == training:
									field[i][z] = x69
									if event.button == 3: #right click
										field[i][z] = o
										last_move[0] = 'o'
										last_move[1], last_move[2] = i,z
									elif event.button == 2: #Middle click
										last_move = ['',0,0]
										field[i][z] = 0
									else:
										last_move = ['x', 0,0]

			for button in gui_button.elements:
				if button.status and game_state in button.frame:
					if x >= button.coords[0] and x <= button.coords[0] + button.size[0] and y >= button.coords[1] and y <= button.coords[1] + button.size[1]:
						button.trigger_function(*button.arguments)
				else:
					continue
	victory_text = ''
	if game_state == game_over and end_time > time():
		if winner in ['o', 'x']:
			victory_text = "Player: "+ winner + " won!"
	elif game_state == game_over and end_time < time():
		start_game(game_mode)

	#Graphics goes here
	screen.fill(darkgrey)

	for button in gui_button.elements:
		if button.status and game_state in button.frame:
			arial_font = pygame.font.Font(pygame.font.get_default_font(), button.text_size)
			surface = arial_font.render(button.text, True, white)
			button_color = button.color
			if button.mousehover():
				button_color = button.hover_color
			pygame.draw.rect(screen, button_color, (button.coords[0], button.coords[1], button.size[0], button.size[1]))
			screen.blit(surface, (button.coords[0] + 6, button.coords[1] + 6))

	if game_state != game_inmenu:

		arial_font = pygame.font.Font(pygame.font.get_default_font(), 12)
		string = "Moves made: " + str(moves) + "   " + victory_text
		rendering = arial_font.render(string, True, white)
		screen.blit(rendering, (1,1))

		pygame.draw.rect(screen, white, (game_field_x, game_field_y, SCREEN_WIDTH - game_field_x - 10, SCREEN_HEIGHT - game_field_y - 10), True)
		
		pygame.draw.line(screen, white, (game_field_x + (SCREEN_WIDTH-game_field_x)/3, game_field_y), (game_field_x + (SCREEN_WIDTH-game_field_x)/3, SCREEN_HEIGHT - 11))
		
		pygame.draw.line(screen, white, (game_field_x + ((SCREEN_WIDTH-game_field_x)/3) * 2, game_field_y), (game_field_x + ((SCREEN_WIDTH-game_field_x)/3) *2, SCREEN_HEIGHT - 11))
		
		pygame.draw.line(screen, white, (game_field_x, game_field_y +(SCREEN_HEIGHT-game_field_y)/3), (SCREEN_WIDTH - 11,  game_field_y +(SCREEN_HEIGHT-game_field_y)/3))
		
		pygame.draw.line(screen, white, (game_field_x, game_field_y +(SCREEN_HEIGHT-game_field_y)/3 * 2), (SCREEN_WIDTH - 11,  game_field_y +(SCREEN_HEIGHT-game_field_y)/3 * 2))

		for i in range(len(field)):
			for y in range(len(field[i])):
				item = field[i][y]
				if item != 0:
					x_axis = int(game_field_x + (rectangle_w / 2) + (rectangle_w * y))
					y_axis = int(game_field_y + (rectangle_h / 2) + (rectangle_h * i))
					font_size = 36
					X_FONT = pygame.font.Font(pygame.font.get_default_font(), font_size)

					if item == o:
						text = X_FONT.render('O', True, white)
					elif item == x69:
						text = X_FONT.render('X', True, white)

					screen.blit(text, (x_axis - font_size/2,y_axis - font_size/2))

	elif game_state == game_inmenu:
		title = "Tic-tac-toe711"
		credits = "by adri711"
		title_size = 34
		title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
		credits_font = pygame.font.Font(pygame.font.get_default_font(), 12)
		credits_gui = credits_font.render(credits, True, white)
		title_gui  = title_font.render(title, True, red)
		screen.blit(title_gui, ( int(SCREEN_WIDTH / 2 - len(title) * title_size / 4), 26))
		screen.blit(credits_gui, ( int(SCREEN_WIDTH / 2), 69))
	pygame.display.flip()