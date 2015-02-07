import pygame, sys
import constants
from laser import Laser
pygame.init()

class Player:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/playership.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = 0
		self.change_y = 0

	def update(self):
		self.rect.x += self.change_x
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.right > constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
		self.rect.y += self.change_y
		for enemy in self.enemy_list:
			if self.rect.colliderect(enemy.rect):
				pygame.quit()
				sys.exit()

	def changespeed(self, x, y):
		self.change_x += x
		self.change_y += y

	def shoot(self):
		self.laser_list.append(Laser(self.rect.centerx, self.rect.top, -5, self))
