import pygame

class Doge():

	def _init_(self, screen):
		"""Initialize doge and set starting position"""
		self.screen = screen
		
		#load ship and get its rect.
		self.image = pygame.image.load('images/doge_small.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start each new doge at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the doge at its current location."""
		self.screen.blit(self.image, self.rect)
