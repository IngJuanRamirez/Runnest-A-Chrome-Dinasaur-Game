# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# main.py
import pygame

# Libraries
from player import Player # Player Sprite

class Runnest:
    def __init__(self) -> None:
        self.width = 500
        self.height = 500

        # Initialize Pygame
        pygame.init()
        
        # Window Title
        pygame.display.set_caption("Runnest")
        # Default background, until changed
        self.WHITE_COLOR_SCREEN = [255, 255, 255]
        # s
        self.screen = pygame.display.set_mode([self.width, self.height])
        # Clock time
        self.clock = pygame.time.Clock()
        # Flag loop
        self.running = True

        # == Create the player ==
        self.player = Player(x=50, y=self.height - 60) # 'y' is the player's height

        # New group of sprites
        self.all_sprites = pygame.sprite.Group()
        # Add player sprite
        self.all_sprites.add(self.player)


    def _loop(self) -> None:
        """Main loop of the game"""
        while(self.running):
            # Events of the game
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Update all sprites
            self.all_sprites.update()

            # Refresh the screen
            self.screen.fill(self.WHITE_COLOR_SCREEN)
            # Draw all spites
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60) # 60fps, for now.

        # Pygame ends
        pygame.quit()

    def run(self) -> None:
        """Start the game"""
        self._loop()

if __name__ == "__main__":
    my_game = Runnest()
    my_game.run()