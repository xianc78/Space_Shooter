import pygame
import constants
from explosion import Explosion
from laser import Laser
pygame.init()

class Enemy:
	def __init__(self, x, y):
		self.image = pygame.image.load("resources/enemyship.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_y = 5
		self.reload_time = constants.RELOAD_TIME

	def update(self):
		self.reload_time -= 1
		self.rect.y += self.change_y
		if self.inLineOfSight() and self.reload_time <= 0:
			self.shoot()
			self.reload_time = constants.RELOAD_TIME
		for laser in self.laser_list:
			if self.rect.colliderect(laser.rect):
				if laser.ship == self.player:
					try:
						self.explosion_list.append(Explosion(self.rect.centerx, self.rect.centery))
						self.player.score += 1
						self.enemy_list.remove(self)
						self.laser_list.remove(laser)
					except ValueError:
						pass
				else:
					pass
		if self.rect.top > constants.SCREEN_HEIGHT:
			self.enemy_list.remove(self)

	def inLineOfSight(self):
		return (self.rect.centerx >= self.player.rect.left) and (self.rect.centerx <= self.player.rect.right)

	def shoot(self):
		self.laser_list.append(Laser(self.rect.centerx, self.rect.centery + 54, 7, self))
