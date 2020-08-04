'''
	Tic-tac-toe - Master
	Author: adri711
	Language: Python
	Written on: 28/07/2020
'''
import sys, pygame
from time import time

pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')

game_inprocess = 0
game_over = 1
end_time = time()
winner = 0

game_state = game_inprocess

SCREEN_HEIGHT = 420
SCREEN_WIDTH = 420

game_field_x = 62
game_field_y = 62

moves = 0

field = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

#colors 
white = 255, 255, 255
black = 0, 0, 0
silver = 192,192,192
darkgrey = 32,32,32
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

def game_check(game_list):
	final_result = '0'
	for row in game_list:
		result = multiple_char_check(row)
		if result == True and row[0] != '0':
			if row[0] == 'o':
				return 'o'
			elif row[0] == 'x':
				return 'x'
		else:
			final_result = '0'
	for i in range(len(game_list)):
		row = ''
		for j in range(len(game_list)):
			row += game_list[j][i]
		result = multiple_char_check(row)
		if result == False:
			final_result = '0'
		else:
			if row[0] == 'o':
				return 'o'
			elif row[0] == 'x':
				return 'x'
	row = game_list[0][0] + game_list[1][1] + game_list[2][2]
	if multiple_char_check(row):
		if row[0] == 'o':
			return 'o'
		elif row[0] == 'x':
			return 'x'
	row = game_list[0][2] + game_list[1][1] + game_list[0][2]
	if multiple_char_check(row):
		if row[0] == 'o':
			return 'o'
		elif row[0] == 'x':
			return 'x'
	return 	final_result

while True:
	rectangle_w = (SCREEN_WIDTH-game_field_x) / 3
	rectangle_h = (SCREEN_HEIGHT-game_field_y) / 3
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			if game_state == game_inprocess:
				x, y = pygame.mouse.get_pos()
				for i in range(len(field)):
					for z in range(len(field[i])):
						if game_field_x + rectangle_w * z <= x and game_field_x + rectangle_w * z + rectangle_w >= x:
							if game_field_y + rectangle_h * i <= y and game_field_y + rectangle_h * i + rectangle_h >= y:
								if field[i][z] == '0':
									field[i][z] = 'x'
									if (moves + 1) % 2 == 0:
										field[i][z] = 'o'
									moves+=1

									result=game_check(field)
									if result == 'x':
										winner = 'x'
										game_state = game_over
										end_time = time() + 3

									elif result =='o':
										winner = 'o'
										game_state = game_over
										end_time = time() + 3
									else:
										if moves >= 9:
											game_state = game_over
											end_time = time() + 3
											winner = "It's a tie."
	''' Drawings lmfao'''
	screen.fill(darkgrey)
	arial_font = pygame.font.Font(pygame.font.get_default_font(), 12)
	string = "Moves made: " + str(moves)
	rendering = arial_font.render(string, True, white)
	screen.blit(rendering, (1,1))
	if game_state == game_over and end_time > time():
		if winner == 'o' or winner == 'x':
			string = "Player: "+ winner + " won!"
		else:
			string = winner
		rendering = arial_font.render(string, True, white)
		screen.blit(rendering, (100, 1))
	elif game_state == game_over and end_time < time():
		game_state = game_inprocess
		moves = 0
		for i in range(len(field)):
			for j in range(len(field)):
				field[i][j] = '0'
	#Graphics bae graphics :D
	pygame.draw.rect(screen, white, (game_field_x, game_field_y, SCREEN_WIDTH - game_field_x - 10, SCREEN_HEIGHT - game_field_y - 10), True)
	
	pygame.draw.line(screen, white, (game_field_x + (SCREEN_WIDTH-game_field_x)/3, game_field_y), (game_field_x + (SCREEN_WIDTH-game_field_x)/3, SCREEN_HEIGHT - 11))
	
	pygame.draw.line(screen, white, (game_field_x + ((SCREEN_WIDTH-game_field_x)/3) * 2, game_field_y), (game_field_x + ((SCREEN_WIDTH-game_field_x)/3) *2, SCREEN_HEIGHT - 11))
	
	pygame.draw.line(screen, white, (game_field_x, game_field_y +(SCREEN_HEIGHT-game_field_y)/3), (SCREEN_WIDTH - 11,  game_field_y +(SCREEN_HEIGHT-game_field_y)/3))
	
	pygame.draw.line(screen, white, (game_field_x, game_field_y +(SCREEN_HEIGHT-game_field_y)/3 * 2), (SCREEN_WIDTH - 11,  game_field_y +(SCREEN_HEIGHT-game_field_y)/3 * 2))

	for i in range(len(field)):
		for y in range(len(field[i])):
			item = field[i][y]
			if item != '0':
				x_axis = int(game_field_x + (rectangle_w / 2) + (rectangle_w * y))
				y_axis = int(game_field_y + (rectangle_h / 2) + (rectangle_h * i))

				if item == 'o':
					pygame.draw.circle(screen, white, (x_axis,y_axis), 24)

				elif item == 'x':
					font_size = 36
					X_FONT = pygame.font.Font(pygame.font.get_default_font(), font_size)
					text = X_FONT.render('X', True, white)
					screen.blit(text, (x_axis - font_size/2,y_axis - font_size/2))

	pygame.display.flip()