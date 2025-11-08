# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# main.py
import pygame

# Libraries
from player import Player # Player sprite
from ground import Ground # Ground level

class Runnest:
    def __init__(self) -> None:
        self.width = 800
        self.height = 500

        # == Ground Constants ==
        self.GROUND_HEIGHT = 80
        self.GROUND_Y = self.height - self.GROUND_HEIGHT

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

        # == Crete the ground
        self.ground = Ground(x=0, y=self.GROUND_Y, width=self.width, height=self.GROUND_HEIGHT)

        # == Create the player ==
        self.player = Player(x=50, y=0) # 'y' is temporal
        # Use the ground to posisionate the player
        self.player.rect.bottom = self.ground.rect.top

        # New group of sprites
        self.all_sprites = pygame.sprite.Group()
        # Add player sprite
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground)

    def _loop(self) -> None:
        """Main loop of the game"""
        while(self.running):
            # Events of the game
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                # Inputs
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # Space Key
                        self.player.jump()

            # Update all sprites
            self.all_sprites.update(self.ground.rect)

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