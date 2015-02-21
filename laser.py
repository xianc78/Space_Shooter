import pygame
import constants
pygame.init()

class Laser:
	def __init__(self, x, y, change_y, ship):
		self.image = pygame.image.load("resources/laser.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.change_y = change_y
		if self.change_y > 0:
			self.image = pygame.transform.flip(self.image, False, True)
		self.ship = ship

	def update(self):
		self.rect.y += self.change_y
		if (self.rect.top < 0) or (self.rect.bottom > constants.SCREEN_HEIGHT):
			self.laser_list.remove(self)
