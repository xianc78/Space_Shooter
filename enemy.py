import pygame
import constants
pygame.init()

class Enemy:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/enemyship.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_y = 5

	def update(self):
		self.rect.y += self.change_y
		for laser in self.laser_list:
			if self.rect.colliderect(laser.rect):
				try:
					self.enemy_list.remove(self)
					self.laser_list.remove(laser)
				except ValueError:
					pass
		if self.rect.bottom > constants.SCREEN_HEIGHT:
			self.enemy_list.remove(self)
