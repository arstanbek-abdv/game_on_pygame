import sys
import pygame 

class AlienInvasion:
    # Overall class to manage the game
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock() # Clock ensures that the game will run across systems consistently by managing (slowing or speeding up FPS)
        self.bg_color = (230,230,230)
    def run_game(self):
        # Start the main loop for the game
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip() # Make the most recently drawn screen visble
            self.clock.tick(60)
            self.screen.fill(self.bg_color)
# Instantiating a game class and running the game 
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
