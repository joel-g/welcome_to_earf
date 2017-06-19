import sys

import pygame

from WtE_settings import Settings
from doge import Doge

def run_game():c
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode ((1200, 800))
pygame.display.set_caption("Welcome to Earf!")
bg_color = (6, 174, 198)

# Make a doge
doge = Doge(screen)


# Main Loop of Game	
while True:

		# Watch for user input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		screen.fill(bg_color)
		doge.blitme()
						
		# Redraw screen		
		pygame.display.flip()
		
run_game()
