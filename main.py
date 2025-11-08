# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# main.py
import pygame

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

    def _loop(self) -> None:
        """Main loop of the game"""
        while(self.running):
            # Events of the game
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Refresh the screen
            self.screen.fill(self.WHITE_COLOR_SCREEN)
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