import pygame, sys
import constants
import random
from player import Player
from enemy import Enemy
from laser import Laser
from explosion import Explosion
from pygame.locals import *
pygame.init()

# Creating the window and settign the caption and icon
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("resources/playership.png")
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

retreat_time = constants.RETREAT_TIME

player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT - 75)

paused = False

# Creating game objects and groups
# Todo: organize this block of code.
laser_list = []
explosion_list = []
player.laser_list = laser_list
Enemy.player = player
player.explosion_list = explosion_list
Enemy.laser_list = laser_list
Enemy.explosion_list = explosion_list
enemy_list = [Enemy(random.randint(0, constants.SCREEN_WIDTH), -75) for i in range(0, 3)]
player.enemy_list = enemy_list
Enemy.enemy_list = enemy_list
Laser.laser_list = laser_list
Laser.explosion_list = explosion_list
Explosion.explosion_list = explosion_list

while True:
	# Draw the images
	screen.fill(constants.BLACK)
	screen.blit(player.image, (player.rect.x, player.rect.y))
	for enemy in enemy_list:
		screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
	for laser in laser_list:
		screen.blit(laser.image, (laser.rect.x, laser.rect.y))
	for explosion in explosion_list:
		screen.blit(explosion.image, (explosion.rect.x, explosion.rect.y))

	# Check for key events	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == K_LEFT:
				player.changespeed(-10, 0)
			elif event.key == K_RIGHT:
				player.changespeed(10, 0)
			elif event.key == K_SPACE:
				player.shoot()
			elif event.key == K_p:
				paused = True
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				player.changespeed(10, 0)
			elif event.key == K_RIGHT:
				player.changespeed(-10, 0)
	while paused:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				elif event.key == K_p:
					paused = False
	# Update game objects			
	player.update()
	for enemy in enemy_list:
		enemy.update()
	for laser in laser_list:
		laser.update()
	for explosion in explosion_list:
		explosion.update()
	retreat_time -= 1
	if retreat_time <= 0:
		enemy_list.append(Enemy(random.randint(0, constants.SCREEN_WIDTH - 112), -75))
		retreat_time = constants.RETREAT_TIME
	pygame.display.update()
	clock.tick(constants.FPS)
