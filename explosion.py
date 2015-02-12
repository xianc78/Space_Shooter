import pygame
import constants

class Explosion:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/explosion.png")
		self.image.set_colorkey(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.life = 20

	def update(self):
		self.life -= 1
		if self.life <= 0:
			self.explosion_list.remove(self)
