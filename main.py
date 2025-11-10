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
        self.GAME_SPEED = 5

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

        # Create the groups
        self.ground_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # == Create the ground ==
        # Ground 1
        self.ground1 = Ground(0, self.GROUND_Y, self.width, self.GROUND_HEIGHT, self.GAME_SPEED, self.ground_group, self.all_sprites)
        # Ground 2
        self.ground2 = Ground(self.width, self.GROUND_Y, self.width, self.GROUND_HEIGHT, self.GAME_SPEED, self.ground_group, self.all_sprites)
        # == WARNING ==
        # I had to change the color of the second ground to view the transition of the ground's group
        self.ground2.image.fill((0, 0, 255))

        # == Create the player ==
        self.player = Player(50, 0, self.all_sprites) # 'y' is temporal
        # Use the ground to posisionate the player
        self.player.rect.bottom = self.ground1.rect.top

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
                        self.player.jump() # Player jumping
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.bend() # Player Crouching down
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.stand_up()

            # Update all sprites
            self.all_sprites.update(self.ground_group)

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