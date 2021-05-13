import pygame
import os
import time 
import random
import time
pygame.font.init()


WIDTH, HEIGHT = 2560, 1440
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
WHITE = (255,255,255)

pygame.display.set_caption("pong")

# load images 
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_ground.png")), (WIDTH,HEIGHT))
BALL = pygame.image.load(os.path.join("assets", "ball.png"))
PLAYER = pygame.image.load(os.path.join("assets", "player.png"))
WALL = pygame.image.load(os.path.join("assets", "wall.png"))



def main():
	run = True
	FPS = 60
	main_font = pygame.font.SysFont("comicsans", 200)
	wait_start = True

	clock = pygame.time.Clock()
	

	class Player:
		def __init__(self, img, score_position_x, score_position_y, x, y = HEIGHT/2, vel = 10, starting_score = 0):
			self.img = img 
			self.y = y 
			self.x = x 
			self.vel = vel
			self.mask = pygame.mask.from_surface(self.img)
			self.score = starting_score = 0
			self.score_position_x = score_position_x
			self.score_position_y = score_position_y

		def draw_player(self, window=WIN):
			self.score_label = main_font.render(f"{self.score}", 1, WHITE)

			if self.score_position_x < WIDTH/2 - 10:
				self.score_position = (self.score_position_x - self.score_label.get_width(), self.score_position_y)
			else:
				self.score_position = (self.score_position_x, self.score_position_y)

			window.blit(self.img, (self.x, self.y))
			window.blit(self.score_label, self.score_position)
			

	class Ball:
		def __init__(self, img, x=WIDTH/2, y=HEIGHT/2, x_vel = -10, angle_range = (-10, 10)):
			self.img = img
			self.x = x 
			self.y = y 
			self.x_vel = x_vel
			self.y_vel = -10#random.randint(angle_range[0],angle_range[1])
			self.mask = pygame.mask.from_surface(self.img)

		def draw_ball(self, window=WIN):
			window.blit(self.img, (self.x, self.y))

	class Wall:
		def __init__(self, img, x, y):
			self.img = img
			self.x = x
			self.y = y
			self.mask = pygame.mask.from_surface(self.img)

		def draw_wall(self, window=WIN):
			window.blit(self.img, (self.x,self.y))




	player1 = Player(PLAYER, WIDTH/2 - 100 , 70, 100)
	player2 = Player(PLAYER, WIDTH/2 + 100, 70, WIDTH - 100)
	ball = Ball(BALL)
	wall1 = Wall(WALL, 100, 30)
	wall2 = Wall(WALL, 100, HEIGHT-70)


	def player_ball_check(players = [player1, player2], ball=ball):
		for player in players:
			offset_x = int(ball.x - player.x)
			offset_y = int(ball.y - player.y)

			if player.mask.overlap(ball.mask, (offset_x, offset_y)) != None:
				ball.x_vel = ball.x_vel * -1
		
	def wall_ball_check(walls = [wall1, wall2], ball=ball):
		for wall in walls:
			offset_x = int(ball.x - wall.x)
			offset_y = int(ball.y - wall.y)

			if wall.mask.overlap(ball.mask, (offset_x, offset_y)) != None:
				ball.y_vel = ball.y_vel * -1

	def move_ball():
		ball.x += ball.x_vel
		ball.y += ball.y_vel


	def check_for_score(ball=ball):
		if ball.x < 100:
			player2.score += 1
			ball.x = WIDTH/2
			ball.y = HEIGHT/2

		if ball.x > WIDTH -100:
			player1.score += 1
			ball.x = WIDTH/2
			ball.y = HEIGHT/2





	def redraw_window():
		WIN.blit(BG, (0,0))

		move_ball()
		#collision check
		player_ball_check()
		wall_ball_check()

		check_for_score()

		ball.draw_ball()
		player1.draw_player()
		player2.draw_player()
		wall1.draw_wall()
		wall2.draw_wall()
		
		pygame.display.update()

	while run:
		clock.tick(FPS)
		redraw_window()
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] and player1.y > 0:
			player1.y -= player1.vel

		if keys[pygame.K_s] and player1.y < HEIGHT - PLAYER.get_height():
			player1.y += player1.vel

		if keys[pygame.K_UP] and player2.y> 0:
			player2.y -= player2.vel
		
		if keys[pygame.K_DOWN] and player2.y < HEIGHT - PLAYER.get_height():
			player2.y += player2.vel 








main()