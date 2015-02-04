import pygame, sys
import constants
import random
from player import Player
from enemy import Enemy
from laser import Laser
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), FULLSCREEN)
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

retreat_time = constants.RETREAT_TIME

player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT - 75)

# Creating game objects and groups
laser_list = []
player.laser_list = laser_list
Enemy.laser_list = laser_list
enemy_list = [Enemy(random.randint(0, constants.SCREEN_WIDTH), 0) for i in range(0, 3)]
player.enemy_list = enemy_list
Enemy.enemy_list = enemy_list
Laser.laser_list = laser_list

while True:
	# Draw the images
	screen.fill(constants.BLACK)
	screen.blit(player.image, (player.rect.x, player.rect.y))
	for enemy in enemy_list:
		screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
	for laser in laser_list:
		screen.blit(laser.image, (laser.rect.x, laser.rect.y))

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
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				player.changespeed(10, 0)
			elif event.key == K_RIGHT:
				player.changespeed(-10, 0)
	# Update game objects			
	player.update()
	for enemy in enemy_list:
		enemy.update()
	for laser in laser_list:
		laser.update()
	retreat_time -= 1
	if retreat_time <= 0:
		for i in range(0, 3):
			enemy_list.append(Enemy(random.randint(0, constants.SCREEN_WIDTH), 0))
		retreat_time = constants.RETREAT_TIME
	pygame.display.update()
	clock.tick(constants.FPS)
