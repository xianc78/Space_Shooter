import pygame, sys
import constants
from laser import Laser
from explosion import Explosion
pygame.init()

laserSound = pygame.mixer.Sound("resources/laser.wav")

class Player:
	def __init__(self, x, y):
		try:
			self.image = pygame.image.load("resources/playership.png").convert_alpha()
		except ValueError:
			print "playership.png has been deleted."
			raw_input("<press enter>")
			pygame.quit()
			sys.exit()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = 0
		self.change_y = 0
		self.score = 0

	def update(self):
		self.rect.x += self.change_x
		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.right > constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
		self.rect.y += self.change_y
		for enemy in self.enemy_list:
			if self.rect.colliderect(enemy.rect):
				self = Explosion(self.rect.centerx, self.rect.centery)
				pygame.display.update(self.rect)
				pygame.time.wait(500)
				pygame.quit()
				sys.exit()
		for laser in self.laser_list:
			if self.rect.colliderect(laser.rect) and laser.ship != self:
				pygame.quit()
				sys.exit()

	def changespeed(self, x, y):
		self.change_x += x
		self.change_y += y

	def shoot(self):
		self.laser_list.append(Laser(self.rect.centerx, self.rect.top, -7, self))
		laserSound.play()
